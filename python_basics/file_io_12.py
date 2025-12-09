"""
Assignment 12: File I/O and Data Persistence

Implement a log analysis system that reads log files, processes entries,
handles parsing errors gracefully, and writes analysis results to output files.

Instructions:
- Implement the parse_log_file function to read and parse log entries
- Each log line format: "TIMESTAMP|LEVEL|MESSAGE" (e.g., "2025-01-15 10:30:45|ERROR|Connection failed")
- Handle file not found, encoding errors, and malformed log entries
- Implement the analyze_logs function to generate statistics
- Use context managers (with statement) for file operations
- Support appending analysis results without overwriting existing data
- Return structured analysis with error counts by log level
"""

from typing import List, Dict, Tuple, Optional


def parse_log_file(file_path: str) -> Tuple[List[Dict], List[str]]:
    """
    Parse a log file and extract structured log entries.
    
    Args:
        file_path: Path to the log file
    
    Returns:
        Tuple of (log_entries, parse_errors)
        - log_entries: List of dicts with keys 'timestamp', 'level', 'message'
        - parse_errors: List of error messages for malformed entries
    
    Format:
        Each line should be: "TIMESTAMP|LEVEL|MESSAGE"
        LEVEL can be: DEBUG, INFO, WARNING, ERROR, CRITICAL
    
    Error Handling:
        - Catch FileNotFoundError if file doesn't exist
        - Catch UnicodeDecodeError for encoding issues
        - Skip malformed lines and add them to parse_errors
        - Always use context managers for file operations
    """
    # TODO: Implement this function
    pass


def analyze_logs(log_entries: List[Dict]) -> Dict:
    """
    Analyze parsed log entries and generate statistics.
    
    Args:
        log_entries: List of log entry dictionaries
    
    Returns:
        Dict with keys:
        - 'total_entries': Total number of log entries
        - 'by_level': Dict with level counts (e.g., {'ERROR': 5, 'INFO': 3})
        - 'critical_messages': List of messages with CRITICAL level
        - 'error_messages': List of messages with ERROR level
    """
    # TODO: Implement this function
    pass


def write_analysis_report(output_path: str, analysis: Dict, mode: str = 'w') -> None:
    """
    Write analysis results to an output file.
    
    Args:
        output_path: Path to write the report
        analysis: Analysis dictionary from analyze_logs
        mode: 'w' for write (overwrite), 'a' for append
    
    Implementation:
        - Use context manager for file writing
        - Format output as readable text
        - Include timestamp header in report
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def create_sample_log_file():
    """Create a sample log file for testing."""
    sample_logs = """2025-01-15 10:30:45|INFO|Application started
2025-01-15 10:30:46|DEBUG|Loading configuration from config.ini
2025-01-15 10:30:47|INFO|Database connection established
2025-01-15 10:30:48|WARNING|Cache is not responding, using fallback
2025-01-15 10:30:50|ERROR|Failed to fetch user data from API
2025-01-15 10:30:51|INFO|Retrying API request
2025-01-15 10:30:55|ERROR|API request timeout after 5 seconds
2025-01-15 10:30:56|CRITICAL|Database connection lost
2025-01-15 10:31:00|INFO|Attempting database reconnection
2025-01-15 10:31:05|ERROR|Reconnection failed, max retries exceeded
This line is malformed and should be skipped
2025-01-15 10:31:10|INFO|Starting fallback mode
2025-01-15 10:31:15|WARNING|Operating in limited functionality mode
2025-01-15 10:31:20|INFO|Background service started"""
    
    with open('/tmp/test_logs.txt', 'w') as f:
        f.write(sample_logs)
    
    return '/tmp/test_logs.txt'


def run_tests():
    """Run test cases for file I/O."""
    
    print("Test 1: Parse valid log file")
    log_file = create_sample_log_file()
    entries, errors = parse_log_file(log_file)
    print(f"  Parsed {len(entries)} entries with {len(errors)} errors")
    if errors:
        print(f"  Parse errors: {errors}\n")
    
    print("Test 2: Analyze logs")
    analysis = analyze_logs(entries)
    print(f"  Total entries: {analysis['total_entries']}")
    print(f"  By level: {analysis['by_level']}")
    print(f"  Critical messages: {len(analysis['critical_messages'])}")
    print(f"  Error messages: {len(analysis['error_messages'])}\n")
    
    print("Test 3: Write analysis report")
    report_path = '/tmp/test_analysis.txt'
    write_analysis_report(report_path, analysis)
    print(f"  Report written to {report_path}")
    
    # Display report content
    with open(report_path, 'r') as f:
        print(f"  Report content:\n{f.read()}\n")
    
    print("Test 4: File not found error handling")
    entries, errors = parse_log_file('/nonexistent/path/file.log')
    print(f"  Handled missing file gracefully")
    print(f"  Entries: {entries}, Errors count: {len(errors)}\n")
    
    print("Test 5: Append to existing report")
    new_analysis = {'total_entries': 5, 'by_level': {'INFO': 3, 'ERROR': 2}, 
                    'critical_messages': [], 'error_messages': ['Error 1', 'Error 2']}
    write_analysis_report(report_path, new_analysis, mode='a')
    print(f"  Appended analysis to report")
    
    with open(report_path, 'r') as f:
        content = f.read()
        print(f"  Report now has {len(content)} characters\n")


if __name__ == '__main__':
    run_tests()
