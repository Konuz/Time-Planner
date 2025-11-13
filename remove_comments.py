#!/usr/bin/env python3
"""
Remove non-essential comments from Plan.html while preserving key comments.
"""

import re

def should_keep_comment(comment_text):
    """Determine if a comment should be kept based on its content."""

    # HTML comments to keep (major section separators)
    keep_patterns = [
        r'Info Modal',
        r'Settings Modal',
        r'Confirm Dialog Modal',
        r'Pomodoro Timer Widget',
        r'Minimized Pomodoro Icon',
        r'TODO Widget',
        r'Minimized TODO Icon'
    ]

    # Patterns for comments to remove (section separators and obvious comments)
    remove_patterns = [
        r'^\s*={3,}\s*$',  # Lines with only ===
        r'^\s*Variables?\s*$',
        r'^\s*Elements?\s*$',
        r'^\s*Section\s*$',
        r'^\s*Tab\s*$',
        r'^\s*constants?\s*$',
        r'Form elements$',
        r'Filter elements$',
        r'Container elements$',
        r'Button elements$',
        r'Modal elements$',
        r'Project management$',
        r'Task type management$',
        r'Pomodoro timer elements$',
        r'Settings inputs$',
        r'TODO widget elements$',
        r'TODO Widget Variables$',
        r'Summary elements$',
        r'Form validation feedback elements$',
        r'Validation constants$',
        r'Validation messages$',
        r'Internationalization',
        r'^\s*i18n\s*$',
        r'Replace parameters',
        r'Update document language',
        r'Update language button',
        r'Single DOM traversal',
        r'Handle data-i18n',
        r'Update Todo tooltips',
        r'Refresh displays',
        r'Fail silently',
        r'Update tooltips',
        r'Todo widget$',
        r'Settings modal$',
        r'Pomodoro Timer Variables$',
        r'Drag.*resize runtime state',
        r'Ustaw stan',
        r'Dodaj event listener',
        r'Przywróć poprzednią',
        r'Zachowaj stan',
        r'Wyczyść kontener',
        r'Generuj filtry',
        r'Update cache reference',
        r'Ponownie podepnij',
        r'Ukryj wszystkie',
        r'Usuń aktywny',
        r'Pokaż wybraną',
        r'Zaznacz aktywny',
        r'Upewnij się',
        r'^\s*Reset\s*$',
        r'Settings are applied',
        r'Months$',
        r'Actions$',
        r'Messages$',
        r'Table headers$',
        r'Pomodoro$',
        r'Pomodoro notifications$',
        r'Summary$',
        r'Settings modal$',
        r'Section visibility$',
        r'Form labels$',
        r'Entries list$'
    ]

    # Check if comment should be removed
    for pattern in remove_patterns:
        if re.search(pattern, comment_text, re.IGNORECASE):
            return False

    # JavaScript comments to keep (explain important logic)
    keep_js_patterns = [
        r'Fixed column widths for consistent header positioning',
        r'Allow text wrapping in Actions column for buttons',
        r'Maintain fixed layout on mobile',
        r'LOCALSTORAGE MANAGEMENT WITH ERROR HANDLING',
        r'END LOCALSTORAGE MANAGEMENT',
        r'Constrain widget position and size to viewport boundaries',
        r'Clamp position to viewport boundaries',
        r'Ensures:.*<=.*',
        r'Unified widget synchronization function.*eliminates.*duplication',
        r'Safe:.*textContent.*prevent XSS',
        r'Poniedziałek jako pierwszy dzień tygodnia',
        r'Monday as first day of week',
        r'Backward compatibility',
        r'Debounce timers for batch saves',
        r'Safe localStorage save with error handling',
        r'Handle storage quota exceeded',
        r'Show storage error to user',
        r'Use provided dimensions or fallback',
        r'Always clean up timer reference to prevent memory leak',
        r'Handle quota exceeded',
        r'Try to free up space',
        r'In this case.*won.*t remove user data',
        r'Other errors.*private browsing',
        r'Event delegation handler.*prevents memory leaks',
        r'Single event delegation handler.*memory leak fix',
        r'Remove old event delegation handler',
        r'Memory leak fix',
        r'Preserve reference',
        r'ES6\+:.*nullish coalescing',
        r'IMPORTANT:',
        r'NOTE:',
        r'WARNING:',
        r'SECURITY:',
        r'Rebuild Map for O\(1\) lookups',
        r'Delete pending Todo task',
        r'Cache all filter states',
        r'Add tooltip with full project name',
        r'Update show more button',
        r'Use DocumentFragment for better performance',
        r'Single DOM update',
        r'Walidacja',
        r'Validation',
        r'Check if all are selected',
        r'Only constrain visible',
        r'Only update if position changed',
        r'Ensure widget stays within viewport',
        r'Insert with auto-sorting',
        r'Find insertion position',
        r'Reorder all tasks',
        r'Clear form',
        r'Clear lists',
        r'Separate tasks',
        r'Render dated',
        r'Fill task number field',
        r'Store the task ID',
        r'Scroll to form',
        r'Just delete',
        r'Copy description',
        r'Show notification',
        r'Note: Task is NOT deleted',
        r'Keep browser cursor',
        r'Store the source list type',
        r'Setting payload keeps',
        r'Firefox/Safari treat',
        r'Prevent dragging between',
        r'Prevent dropping',
        r'Only rebuild order',
        r'Update empty-field class',
        r'Initial check',
        r'Update on input',
        r'Minimized timer is updated',
        r'Start minimized by default',
        r'Add task button',
        r'Delete all button',
        r'Minimize button',
        r'Minimized widget click',
        r'No date checkbox',
        r'Initialize TODO widget'
    ]

    for pattern in keep_patterns:
        if re.search(pattern, comment_text, re.IGNORECASE):
            return True

    for pattern in keep_js_patterns:
        if re.search(pattern, comment_text, re.IGNORECASE):
            return True

    return False

def process_file(filename):
    """Process the HTML file and remove non-essential comments."""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove HTML comments that should not be kept
    def replace_html_comment(match):
        comment_text = match.group(1)
        if should_keep_comment(comment_text):
            return match.group(0)  # Keep the comment
        return ''  # Remove the comment

    content = re.sub(r'<!--(.*?)-->', replace_html_comment, content, flags=re.DOTALL)

    # Remove single-line JavaScript comments that should not be kept
    lines = content.split('\n')
    processed_lines = []

    for line in lines:
        # Check if line contains only a single-line comment (with optional whitespace)
        single_comment_match = re.match(r'^(\s*)//(.*)$', line)
        if single_comment_match:
            comment_text = single_comment_match.group(2)
            if should_keep_comment(comment_text):
                processed_lines.append(line)  # Keep the comment
            # Otherwise skip the line (remove it)
        else:
            # Keep non-comment lines
            processed_lines.append(line)

    content = '\n'.join(processed_lines)

    # Remove multi-line JavaScript comments that should not be kept
    def replace_js_comment(match):
        comment_text = match.group(1)
        if should_keep_comment(comment_text):
            return match.group(0)  # Keep the comment
        return ''  # Remove the comment

    content = re.sub(r'/\*(.*?)\*/', replace_js_comment, content, flags=re.DOTALL)

    # Clean up multiple consecutive blank lines (reduce to max 2)
    content = re.sub(r'\n\n\n+', '\n\n', content)

    return content

if __name__ == '__main__':
    input_file = 'Plan.html'
    output_file = 'Plan.html'

    processed_content = process_file(input_file)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed_content)

    print('Comments removed successfully!')
    print('Key comments explaining important logic have been preserved.')
