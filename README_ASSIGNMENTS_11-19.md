# 🎓 Intermediate & Advanced Python Assignments (11-19)

## 📚 Overview

Nine comprehensive assignments covering intermediate and advanced Python topics have been created to complement the existing basic assignments (1-10).

**Total:** 9 assignments | 2,310+ lines of code | 155+ tests | 2,000+ lines of documentation

---

## 🚀 Quick Start

### 1. Choose Your Assignment
See [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for a quick overview or [COMPLETE_INDEX.md](COMPLETE_INDEX.md) for detailed information.

### 2. Pick a Learning Path

**Sequential (Recommended):**
```
11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19
```

**By Level:**
- Intermediate: 11, 12, 13, 14
- Advanced: 15, 16, 17, 18, 19

**By Interest:**
- Error & Validation: 11, 18
- Data Processing: 12, 13, 15
- Code Organization: 14, 16, 17
- Performance: 15, 19

### 3. Read Assignment Docstring
Each assignment file has comprehensive documentation.

### 4. Implement & Test
```bash
# Run tests for your assignment
pytest tests/test_python_basics/test_XX_*.py -v

# Or run built-in test code
python python_basics/XXX_YYY.py
```

---

## 📋 The 9 Assignments

| # | Title | Difficulty | Time | Key Topics |
|---|-------|-----------|------|-----------|
| 11 | Error Handling | Intermediate | 2-3h | try/except, custom exceptions |
| 12 | File I/O | Intermediate | 2-3h | with statement, file operations |
| 13 | Comprehensions | Intermediate | 3-4h | List/dict comprehensions, lambda |
| 14 | Decorators | Intermediate | 3-4h | @decorator, functools |
| 15 | Iterators/Generators | Advanced | 4-5h | yield, generators, lazy eval |
| 16 | Context Managers | Advanced | 3-4h | __enter__/__exit__, cleanup |
| 17 | OOP Inheritance | Advanced | 3-4h | super(), polymorphism |
| 18 | Type Hinting | Advanced | 2-3h | Type hints, generics |
| 19 | Async Programming | Advanced | 4-5h | async/await, concurrent ops |

---

## 📁 Files Structure

### Assignment Files
```
python_basics/
├── error_handling_11.py
├── file_io_12.py
├── comprehensions_13.py
├── decorators_14.py
├── iterators_generators_15.py
├── context_managers_16.py
├── oop_inheritance_17.py
├── type_hinting_18.py
└── async_programming_19.py
```

### Test Files
```
tests/test_python_basics/
├── test_11_error_handling.py
├── test_12_file_io.py
├── test_13_comprehensions.py
├── test_14_decorators.py
├── test_15_iterators_generators.py
├── test_17_oop_inheritance.py
└── test_18_type_hinting.py
```

### Documentation
- **QUICK_REFERENCE.md** - Quick lookup and patterns
- **COMPLETE_INDEX.md** - Full assignment details
- **INTERMEDIATE_ADVANCED_ASSIGNMENTS.md** - Comprehensive guide
- **ASSIGNMENTS_SUMMARY.md** - Executive overview
- **COMPLETION_REPORT.md** - Work completed summary

---

## 🎯 What You'll Learn

### Intermediate (Assignments 11-14)
- ✅ Write robust code with proper error handling
- ✅ Read and write files safely using context managers
- ✅ Transform data concisely with comprehensions and functional programming
- ✅ Use decorators for cross-cutting concerns

### Advanced (Assignments 15-19)
- ✅ Process large datasets efficiently with generators
- ✅ Manage resources safely with context managers
- ✅ Design scalable class hierarchies with inheritance
- ✅ Write self-documenting code with type hints
- ✅ Build concurrent applications with async/await

---

## 🔨 Implementation Pattern

For each assignment:

1. **Open the assignment file:**
   ```bash
   code python_basics/assignment_XX.py
   ```

2. **Read the docstring** at the top of the file

3. **Find TODO comments** - These mark what to implement

4. **Replace `pass` with code:**
   ```python
   # Before:
   def my_function():
       pass
   
   # After:
   def my_function():
       return "implementation"
   ```

5. **Test your implementation:**
   ```bash
   # Quick test
   python python_basics/assignment_XX.py
   
   # Full test suite
   pytest tests/test_python_basics/test_XX_*.py -v
   ```

---

## ✅ Testing

### Quick Test (Built-in)
Each assignment has a `run_tests()` function:
```bash
python python_basics/assignment_XX.py
```

### Full Test Suite
```bash
# All tests
pytest tests/test_python_basics/ -v

# Specific assignment
pytest tests/test_python_basics/test_11_error_handling.py -v

# Specific test class
pytest tests/test_python_basics/test_17_oop_inheritance.py::TestVehicleBaseClass -v

# With coverage
pytest --cov=python_basics tests/test_python_basics/
```

---

## 📖 Documentation Guide

### For Students
1. Start: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. Pick: Choose an assignment
3. Learn: Read assignment docstring
4. Understand: Read [INTERMEDIATE_ADVANCED_ASSIGNMENTS.md](INTERMEDIATE_ADVANCED_ASSIGNMENTS.md)
5. Code: Implement your solution
6. Test: Run pytest

### For Instructors
1. Overview: [ASSIGNMENTS_SUMMARY.md](ASSIGNMENTS_SUMMARY.md)
2. Details: [COMPLETE_INDEX.md](COMPLETE_INDEX.md)
3. Grading: Use pytest output
4. Extend: Review docstrings for customization points

---

## 💡 Tips for Success

### Getting Started
- Start with Assignment 11 or 13 (good foundations)
- Read the full docstring before coding
- Look at the test file to understand requirements
- Run `run_tests()` in the assignment file for quick feedback

### While Coding
- Follow the docstring specification exactly
- Handle all edge cases mentioned
- Keep functions focused and simple
- Use meaningful variable names
- Add comments for complex logic

### Debugging
- Print intermediate values with `print()`
- Use pytest verbose mode: `pytest -v`
- Check test output for specific failures
- Review test code for expected behavior
- Compare your output with expected results

### Optimization
- Don't over-optimize - correctness first
- Use built-in Python functions (map, filter, etc.)
- Consider memory with generators
- Profile with timing decorators
- But keep code readable!

---

## 🎓 Learning Outcomes

After all 9 assignments, you'll be able to:

1. ✅ Write production-ready Python code
2. ✅ Handle errors gracefully and informatively
3. ✅ Process files and data safely
4. ✅ Write concise, Pythonic transformations
5. ✅ Apply decorators for advanced function composition
6. ✅ Process large datasets efficiently
7. ✅ Manage resources with context managers
8. ✅ Design scalable class hierarchies
9. ✅ Write self-documenting type-hinted code
10. ✅ Build concurrent applications

---

## 📊 Assignment Statistics

| Metric | Value |
|--------|-------|
| Total Assignments | 9 |
| Implementation Code | 2,310+ lines |
| Test Code | 1,500+ lines |
| Documentation | 2,000+ lines |
| Test Methods | 155+ |
| Test Classes | 42 |
| Functions to Implement | 50+ |
| Estimated Time | 25-35 hours |

---

## 🔄 Workflow Example

### Assignment 13 (Comprehensions)
```bash
# 1. Open assignment
cd /Users/yeshwanth/Code/Divami/ml-and-ai-assignments
code python_basics/comprehensions_13.py

# 2. Read docstring - understand what to implement
# 3. Code each function - replace 'pass' with implementation
# 4. Quick test
python python_basics/comprehensions_13.py

# 5. Full test suite
pytest tests/test_python_basics/test_13_comprehensions.py -v

# 6. Review and refactor code
# 7. Final check
pytest tests/test_python_basics/test_13_comprehensions.py -v --cov=python_basics.comprehensions_13
```

---

## 🎯 Success Criteria

✅ Assignment is "done" when:
- [ ] All TODO comments replaced with implementation
- [ ] All test methods pass (green checkmarks)
- [ ] Code follows PEP 8 style
- [ ] All docstrings present
- [ ] No warnings or errors in output
- [ ] Edge cases handled
- [ ] Code is readable and maintainable

---

## 🆘 Troubleshooting

### pytest not found
```bash
pip install pytest
```

### Import errors
- Check Python path includes the repo root
- Verify `__init__.py` files exist
- Try: `export PYTHONPATH=/path/to/repo`

### Test failures
- Read the test output carefully
- Check expected vs actual values
- Review the test code to understand requirements
- Add print() statements to debug

### Timeout issues
- Check for infinite loops
- Reduce sleep times in async assignments
- Increase timeout in pytest config

---

## 📞 Quick Reference

### Common Commands
```bash
# Navigate to repo
cd /Users/yeshwanth/Code/Divami/ml-and-ai-assignments

# Run all tests
pytest tests/test_python_basics/ -v

# Run single assignment test
pytest tests/test_python_basics/test_13_comprehensions.py -v

# Run built-in test
python python_basics/comprehensions_13.py

# View test coverage
pytest --cov=python_basics tests/test_python_basics/

# Watch for changes
pytest-watch tests/test_python_basics/
```

---

## 📚 Recommended Reading Order

1. This README (you're reading it!)
2. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick overview
3. Assignment docstring - Specific details
4. [INTERMEDIATE_ADVANCED_ASSIGNMENTS.md](INTERMEDIATE_ADVANCED_ASSIGNMENTS.md) - Deep dive
5. Test file - Understand requirements
6. Code & implement
7. [COMPLETE_INDEX.md](COMPLETE_INDEX.md) - Additional context

---

## 🎓 After Completing All Assignments

- You'll have built a strong intermediate/advanced Python foundation
- You'll be able to tackle real-world projects
- You'll understand professional Python development patterns
- You'll be ready for specialized topics (web, data science, etc.)
- Consider contributing to open-source projects!

---

## 📝 Notes

- All assignments are self-contained and can be done independently
- But doing them in order builds better understanding
- Don't rush - take time to really understand each concept
- Reread assignments - you'll notice new details
- Experiment beyond the requirements!

---

## 🎯 Final Checklist

- [ ] Read this README
- [ ] Install pytest: `pip install pytest`
- [ ] Choose your first assignment (11 or 13 recommended)
- [ ] Read assignment docstring
- [ ] Implement all functions
- [ ] Run tests: `pytest tests/test_python_basics/test_XX_*.py -v`
- [ ] Review code quality
- [ ] Move to next assignment
- [ ] After 9 assignments - celebrate! 🎉

---

**Ready to start? Pick assignment 11 or 13 and open the file!**

---

*Last Updated: December 8, 2025*  
*Status: Ready for Use*  
*Python: 3.7+*  

For more details, see the comprehensive documentation files in this directory.
