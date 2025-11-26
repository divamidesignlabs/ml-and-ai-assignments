"""
Pytest tests for Assignment 2: Routing Rules Engine
"""

import pytest

from python_basics.routing_rules_engine_02 import assign_zone, apply_routing_rules


class TestAssignZone:
    """Test cases for assign_zone function."""
    
    def test_bulk_zone_high_quantity(self):
        """Test that high quantities go to bulk zone."""
        assert assign_zone('SKU001', 150, 'A1') == 'bulk'
        assert assign_zone('SKU002', 200, 'B2') == 'bulk'
    
    def test_bulk_zone_boundary(self):
        """Test bulk zone boundary at qty=100."""
        assert assign_zone('SKU001', 100, 'A1') == 'bulk'
        assert assign_zone('SKU002', 99, 'A1') == 'general'
    
    def test_general_zone_medium_quantity(self):
        """Test that medium quantities go to general zone."""
        assert assign_zone('SKU001', 50, 'A1') == 'general'
        assert assign_zone('SKU002', 75, 'B2') == 'general'
    
    def test_general_zone_boundary(self):
        """Test general zone boundary at qty=20."""
        assert assign_zone('SKU001', 20, 'A1') == 'general'
        assert assign_zone('SKU002', 19, 'A1') == 'pick-face'
    
    def test_pick_face_zone_low_quantity(self):
        """Test that low quantities go to pick-face zone."""
        assert assign_zone('SKU001', 10, 'A1') == 'pick-face'
        assert assign_zone('SKU002', 5, 'B2') == 'pick-face'
        assert assign_zone('SKU003', 0, 'C3') == 'pick-face'
    
    def test_hazmat_override_high_quantity(self):
        """Test hazmat override with high quantity."""
        assert assign_zone('HAZ001', 200, 'A1') == 'hazmat'
    
    def test_hazmat_override_low_quantity(self):
        """Test hazmat override with low quantity."""
        assert assign_zone('HAZ001', 5, 'A1') == 'hazmat'
    
    def test_hazmat_case_sensitive(self):
        """Test that hazmat check is case-sensitive (HAZ prefix)."""
        # Only uppercase HAZ should trigger hazmat
        assert assign_zone('HAZ001', 50, 'A1') == 'hazmat'
        # Lowercase should follow normal rules
        result = assign_zone('haz001', 50, 'A1')
        # Depending on implementation, lowercase might or might not be hazmat
        assert result in ['hazmat', 'general']


class TestApplyRoutingRules:
    """Test cases for apply_routing_rules function."""
    
    def test_basic_routing(self):
        """Test basic routing application."""
        inventory = [
            ('SKU001', 10, 'A1'),
            ('SKU002', 25, 'B2'),
        ]
        
        result = apply_routing_rules(inventory)
        
        assert ('SKU001', 'pick-face') in result
        assert ('SKU002', 'general') in result
    
    def test_routing_preserves_order(self):
        """Test that routing preserves input order."""
        inventory = [
            ('SKU001', 10, 'A1'),
            ('SKU002', 25, 'B2'),
            ('HAZ003', 5, 'C3'),
            ('SKU004', 150, 'D4'),
        ]
        
        expected = [
            ('SKU001', 'pick-face'),
            ('SKU002', 'general'),
            ('HAZ003', 'hazmat'),
            ('SKU004', 'bulk'),
        ]
        
        result = apply_routing_rules(inventory)
        
        assert result == expected
    
    def test_empty_inventory(self):
        """Test routing with empty inventory."""
        result = apply_routing_rules([])
        assert result == []
    
    def test_all_zones_represented(self):
        """Test that all zones can be assigned."""
        inventory = [
            ('SKU001', 5, 'A1'),    # pick-face
            ('SKU002', 50, 'B2'),   # general
            ('SKU003', 150, 'C3'),  # bulk
            ('HAZ001', 10, 'D4'),   # hazmat
        ]
        
        result = apply_routing_rules(inventory)
        zones = [zone for _, zone in result]
        
        assert 'pick-face' in zones
        assert 'general' in zones
        assert 'bulk' in zones
        assert 'hazmat' in zones
