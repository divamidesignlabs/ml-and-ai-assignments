"""
Pytest tests for Assignment 12: File I/O and Data Persistence
"""

import pytest
import os
from python_basics.file_io_12 import parse_log_file, analyze_logs, write_analysis_report


class TestParseLogFile:
    """Test cases for log file parsing."""
    
    def test_parse_valid_log_file(self, tmp_path):
        """Test parsing a valid log file."""
        log_file = tmp_path / "test.log"
        log_file.write_text("""2025-01-15 10:30:45|INFO|Application started
2025-01-15 10:30:46|ERROR|Connection failed
2025-01-15 10:30:47|WARNING|Timeout detected""")
        
        entries, errors = parse_log_file(str(log_file))
        
        assert len(entries) == 3
        assert len(errors) == 0
        assert entries[0]['level'] == 'INFO'
        assert entries[1]['level'] == 'ERROR'
    
    def test_parse_file_not_found(self):
        """Test handling of missing file."""
        entries, errors = parse_log_file('/nonexistent/file.log')
        
        # Should handle gracefully
        assert isinstance(entries, list)
        assert isinstance(errors, list)
    
    def test_parse_malformed_entries(self, tmp_path):
        """Test parsing with malformed entries."""
        log_file = tmp_path / "malformed.log"
        log_file.write_text("""2025-01-15 10:30:45|INFO|Valid entry
This line is completely malformed
2025-01-15 10:30:46|ERROR|Another valid entry""")
        
        entries, errors = parse_log_file(str(log_file))
        
        assert len(entries) == 2
        assert len(errors) == 1
    
    def test_parse_entry_structure(self, tmp_path):
        """Test that parsed entries have correct structure."""
        log_file = tmp_path / "test.log"
        log_file.write_text("2025-01-15 10:30:45|INFO|Test message")
        
        entries, _ = parse_log_file(str(log_file))
        
        assert len(entries) == 1
        assert 'timestamp' in entries[0]
        assert 'level' in entries[0]
        assert 'message' in entries[0]
    
    def test_parse_various_log_levels(self, tmp_path):
        """Test parsing different log levels."""
        log_file = tmp_path / "levels.log"
        log_file.write_text("""2025-01-15 10:00:00|DEBUG|Debug message
2025-01-15 10:00:01|INFO|Info message
2025-01-15 10:00:02|WARNING|Warning message
2025-01-15 10:00:03|ERROR|Error message
2025-01-15 10:00:04|CRITICAL|Critical message""")
        
        entries, _ = parse_log_file(str(log_file))
        
        levels = [e['level'] for e in entries]
        assert 'DEBUG' in levels
        assert 'INFO' in levels
        assert 'WARNING' in levels
        assert 'ERROR' in levels
        assert 'CRITICAL' in levels


class TestAnalyzeLogs:
    """Test cases for log analysis."""
    
    def test_analyze_empty_logs(self):
        """Test analyzing empty log list."""
        analysis = analyze_logs([])
        
        assert analysis['total_entries'] == 0
        assert analysis['by_level']['ERROR'] == 0
    
    def test_analyze_log_counts(self):
        """Test counting logs by level."""
        entries = [
            {'timestamp': '2025-01-15 10:00:00', 'level': 'INFO', 'message': 'msg1'},
            {'timestamp': '2025-01-15 10:00:01', 'level': 'INFO', 'message': 'msg2'},
            {'timestamp': '2025-01-15 10:00:02', 'level': 'ERROR', 'message': 'msg3'},
            {'timestamp': '2025-01-15 10:00:03', 'level': 'WARNING', 'message': 'msg4'},
        ]
        
        analysis = analyze_logs(entries)
        
        assert analysis['total_entries'] == 4
        assert analysis['by_level']['INFO'] == 2
        assert analysis['by_level']['ERROR'] == 1
        assert analysis['by_level']['WARNING'] == 1
    
    def test_extract_critical_messages(self):
        """Test extraction of critical messages."""
        entries = [
            {'timestamp': '2025-01-15 10:00:00', 'level': 'CRITICAL', 'message': 'Critical failure'},
            {'timestamp': '2025-01-15 10:00:01', 'level': 'INFO', 'message': 'Normal'},
            {'timestamp': '2025-01-15 10:00:02', 'level': 'CRITICAL', 'message': 'System down'},
        ]
        
        analysis = analyze_logs(entries)
        
        assert len(analysis['critical_messages']) == 2
        assert 'Critical failure' in analysis['critical_messages']
        assert 'System down' in analysis['critical_messages']
    
    def test_extract_error_messages(self):
        """Test extraction of error messages."""
        entries = [
            {'timestamp': '2025-01-15 10:00:00', 'level': 'ERROR', 'message': 'Connection timeout'},
            {'timestamp': '2025-01-15 10:00:01', 'level': 'INFO', 'message': 'Normal'},
            {'timestamp': '2025-01-15 10:00:02', 'level': 'ERROR', 'message': 'Parse error'},
        ]
        
        analysis = analyze_logs(entries)
        
        assert len(analysis['error_messages']) == 2


class TestWriteAnalysisReport:
    """Test cases for writing analysis reports."""
    
    def test_write_report_creates_file(self, tmp_path):
        """Test that report file is created."""
        report_path = tmp_path / "report.txt"
        analysis = {
            'total_entries': 10,
            'by_level': {'INFO': 5, 'ERROR': 3},
            'critical_messages': [],
            'error_messages': ['Error 1', 'Error 2']
        }
        
        write_analysis_report(str(report_path), analysis)
        
        assert report_path.exists()
    
    def test_report_contains_analysis_data(self, tmp_path):
        """Test that report contains analysis data."""
        report_path = tmp_path / "report.txt"
        analysis = {
            'total_entries': 42,
            'by_level': {'INFO': 5, 'ERROR': 3},
            'critical_messages': [],
            'error_messages': ['Error 1']
        }
        
        write_analysis_report(str(report_path), analysis)
        
        content = report_path.read_text()
        assert '42' in content or 'total_entries' in content
    
    def test_append_mode(self, tmp_path):
        """Test appending to existing report."""
        report_path = tmp_path / "report.txt"
        
        # Write initial report
        analysis1 = {
            'total_entries': 10,
            'by_level': {},
            'critical_messages': [],
            'error_messages': []
        }
        write_analysis_report(str(report_path), analysis1, mode='w')
        initial_size = len(report_path.read_text())
        
        # Append another report
        analysis2 = {
            'total_entries': 20,
            'by_level': {},
            'critical_messages': [],
            'error_messages': []
        }
        write_analysis_report(str(report_path), analysis2, mode='a')
        
        final_size = len(report_path.read_text())
        assert final_size > initial_size
    
    def test_write_mode_overwrites(self, tmp_path):
        """Test that write mode overwrites existing file."""
        report_path = tmp_path / "report.txt"
        
        # Write initial report
        analysis1 = {
            'total_entries': 10,
            'by_level': {},
            'critical_messages': [],
            'error_messages': []
        }
        write_analysis_report(str(report_path), analysis1, mode='w')
        
        # Write new report with write mode
        analysis2 = {
            'total_entries': 5,
            'by_level': {},
            'critical_messages': [],
            'error_messages': []
        }
        write_analysis_report(str(report_path), analysis2, mode='w')
        
        content = report_path.read_text()
        # Should have the new analysis data
        assert '5' in content or 'total_entries' in content


class TestIntegration:
    """Integration tests combining parsing and analysis."""
    
    def test_parse_and_analyze_workflow(self, tmp_path):
        """Test complete workflow of parsing and analyzing logs."""
        log_file = tmp_path / "test.log"
        log_file.write_text("""2025-01-15 10:00:00|INFO|Started
2025-01-15 10:00:01|ERROR|Failed
2025-01-15 10:00:02|INFO|Retrying
2025-01-15 10:00:03|ERROR|Failed again
2025-01-15 10:00:04|CRITICAL|System down""")
        
        entries, _ = parse_log_file(str(log_file))
        analysis = analyze_logs(entries)
        
        assert analysis['total_entries'] == 5
        assert analysis['by_level']['INFO'] == 2
        assert analysis['by_level']['ERROR'] == 2
        assert len(analysis['critical_messages']) == 1
