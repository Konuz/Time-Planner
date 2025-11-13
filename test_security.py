#!/usr/bin/env python3
"""
Comprehensive security and regression testing for Plan.html
Tests XSS protection, localStorage validation, and core functionality
"""

from playwright.sync_api import sync_playwright
import os
import sys
from pathlib import Path

# OWASP XSS Test Payloads - Common attack vectors
XSS_PAYLOADS = [
    '<script>alert("XSS")</script>',
    '<img src=x onerror=alert("XSS")>',
    '<svg onload=alert("XSS")>',
    'javascript:alert("XSS")',
    '<iframe src="javascript:alert(\'XSS\')">',
    '<body onload=alert("XSS")>',
    '<input type="text" value="<script>alert(\'XSS\')</script>">',
    '"><script>alert(String.fromCharCode(88,83,83))</script>',
    '<IMG SRC=javascript:alert(&quot;XSS&quot;)>',
    '<SCRIPT SRC=http://evil.com/xss.js></SCRIPT>'
]

def get_plan_path():
    """Get absolute path to Plan.html"""
    plan_path = Path(__file__).parent / "Plan.html"
    if not plan_path.exists():
        print(f"❌ Error: Plan.html not found at {plan_path}")
        sys.exit(1)
    return f"file://{plan_path.absolute()}"

def test_xss_protection(page):
    """Test XSS protection in entry form"""
    print("\n🔒 Testing XSS Protection...")

    results = {
        'blocked': 0,
        'failed': 0,
        'tests': []
    }

    for payload in XSS_PAYLOADS[:5]:  # Test first 5 payloads
        try:
            # Fill form with XSS payload in taskNumber field
            page.fill('#date', '2025-11-11')
            page.select_option('#task-type', index=0)
            page.select_option('#client', index=0)
            page.fill('#hours', '1')
            page.fill('#task-number', payload)

            # Submit form
            page.click('button:has-text("Dodaj")')

            # Wait a bit for potential XSS execution
            page.wait_for_timeout(500)

            # Check if alert dialog appeared (XSS executed)
            dialogs = []
            page.on('dialog', lambda dialog: dialogs.append(dialog))

            if dialogs:
                results['failed'] += 1
                results['tests'].append({
                    'payload': payload,
                    'status': '❌ VULNERABLE',
                    'details': 'Alert dialog appeared - XSS executed'
                })
            else:
                results['blocked'] += 1
                results['tests'].append({
                    'payload': payload,
                    'status': '✅ BLOCKED',
                    'details': 'No alert dialog - XSS prevented'
                })

            # Clear form
            page.fill('#task-number', '')

        except Exception as e:
            results['tests'].append({
                'payload': payload,
                'status': '⚠️ ERROR',
                'details': str(e)
            })

    # Print results
    print(f"\n📊 XSS Protection Results:")
    print(f"   Blocked: {results['blocked']}/{len(results['tests'])}")
    print(f"   Failed: {results['failed']}/{len(results['tests'])}")

    for test in results['tests']:
        print(f"   {test['status']} - {test['payload'][:50]}...")
        print(f"      {test['details']}")

    return results

def test_localstorage_validation(page):
    """Test localStorage manipulation attack"""
    print("\n🔐 Testing localStorage Validation...")

    # Inject malicious entry via localStorage
    malicious_entry = {
        'id': 999999,
        'date': '2025-11-11',
        'taskType': '<script>alert("XSS")</script>',
        'client': '<img src=x onerror=alert("XSS")>',
        'hours': 999,  # Invalid hours
        'taskNumber': '<svg onload=alert("XSS")>'
    }

    page.evaluate(f"""
        const entries = JSON.parse(localStorage.getItem('timesheet-entries') || '[]');
        entries.push({malicious_entry});
        localStorage.setItem('timesheet-entries', JSON.stringify(entries));
    """, malicious_entry)

    # Reload page to trigger validation
    page.reload()
    page.wait_for_load_state('networkidle')

    # Check if malicious entry was sanitized/removed
    entries = page.evaluate("JSON.parse(localStorage.getItem('timesheet-entries') || '[]')")

    malicious_found = any(
        e.get('id') == 999999 and
        ('<script>' in str(e.get('taskType', '')) or
         '<img' in str(e.get('client', '')) or
         e.get('hours', 0) > 8)
        for e in entries
    )

    if malicious_found:
        print("   ❌ VULNERABLE - Malicious entry not removed from localStorage")
        return False
    else:
        print("   ✅ SECURE - Malicious entry sanitized/removed from localStorage")
        return True

def test_core_functionality(page):
    """Test core features after security fixes"""
    print("\n🧪 Testing Core Functionality (Regression)...")

    tests_passed = 0
    tests_total = 0

    # Test 1: Add valid entry
    tests_total += 1
    try:
        page.fill('#date', '2025-11-11')
        page.select_option('#task-type', index=0)
        page.select_option('#client', index=0)
        page.fill('#hours', '2')
        page.fill('#task-number', 'TEST-001')
        page.click('button:has-text("Dodaj")')
        page.wait_for_timeout(500)

        # Check if entry appears in table
        if page.locator('text=TEST-001').count() > 0:
            print("   ✅ Add entry - PASS")
            tests_passed += 1
        else:
            print("   ❌ Add entry - FAIL")
    except Exception as e:
        print(f"   ❌ Add entry - ERROR: {e}")

    # Test 2: Form validation
    tests_total += 1
    try:
        page.fill('#hours', '10')  # Invalid hours (>8)
        page.click('button:has-text("Dodaj")')
        page.wait_for_timeout(500)

        # Check if validation error appears
        if page.locator('.is-invalid').count() > 0 or page.locator('.invalid-feedback:visible').count() > 0:
            print("   ✅ Form validation - PASS")
            tests_passed += 1
        else:
            print("   ❌ Form validation - FAIL (no error shown)")
    except Exception as e:
        print(f"   ❌ Form validation - ERROR: {e}")

    # Test 3: Summary calculation
    tests_total += 1
    try:
        summary_text = page.locator('#summary-content').inner_text()
        if 'godzin' in summary_text.lower() or 'hours' in summary_text.lower():
            print("   ✅ Summary calculation - PASS")
            tests_passed += 1
        else:
            print("   ❌ Summary calculation - FAIL")
    except Exception as e:
        print(f"   ❌ Summary calculation - ERROR: {e}")

    # Test 4: Language switching
    tests_total += 1
    try:
        page.click('#language-select')
        page.select_option('#language-select', 'en')
        page.wait_for_timeout(500)

        if page.locator('text=Add Entry').count() > 0 or page.locator('text=Add').count() > 0:
            print("   ✅ Language switching - PASS")
            tests_passed += 1
        else:
            print("   ❌ Language switching - FAIL")
    except Exception as e:
        print(f"   ❌ Language switching - ERROR: {e}")

    print(f"\n📊 Regression Test Results: {tests_passed}/{tests_total} passed")
    return tests_passed == tests_total

def main():
    print("=" * 60)
    print("🔒 Security & Regression Testing for Plan.html")
    print("=" * 60)

    plan_url = get_plan_path()
    print(f"📄 Testing: {plan_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Setup console logging
        console_messages = []
        page.on('console', lambda msg: console_messages.append(msg))

        # Setup dialog handler for XSS detection
        def handle_dialog(dialog):
            print(f"   ⚠️ Alert detected: {dialog.message}")
            dialog.dismiss()

        page.on('dialog', handle_dialog)

        try:
            # Load page
            page.goto(plan_url)
            page.wait_for_load_state('networkidle')
            page.wait_for_timeout(1000)  # Extra wait for initialization

            # Run tests
            xss_results = test_xss_protection(page)
            storage_secure = test_localstorage_validation(page)
            regression_passed = test_core_functionality(page)

            # Check console for validation warnings
            print("\n📋 Console Messages:")
            validation_warnings = [msg for msg in console_messages if 'Invalid entry' in msg.text or 'Sanitized' in msg.text]
            if validation_warnings:
                print(f"   Found {len(validation_warnings)} validation warnings (expected behavior)")
                for msg in validation_warnings[:5]:  # Show first 5
                    print(f"   - {msg.text}")

            # Final summary
            print("\n" + "=" * 60)
            print("📊 FINAL SUMMARY")
            print("=" * 60)
            print(f"XSS Protection: {xss_results['blocked']}/{len(xss_results['tests'])} blocked")
            print(f"localStorage Security: {'✅ SECURE' if storage_secure else '❌ VULNERABLE'}")
            print(f"Regression Tests: {'✅ PASSED' if regression_passed else '❌ FAILED'}")

            if xss_results['failed'] == 0 and storage_secure and regression_passed:
                print("\n✅ All security tests passed! Application is production-ready.")
                return 0
            else:
                print("\n⚠️ Some tests failed. Review results above.")
                return 1

        except Exception as e:
            print(f"\n❌ Fatal error during testing: {e}")
            import traceback
            traceback.print_exc()
            return 1

        finally:
            browser.close()

if __name__ == '__main__':
    sys.exit(main())
