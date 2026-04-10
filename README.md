# AI_Study_Planner_Vityarthi

An intelligent command-line based study planner built using Python that helps students allocate their daily study time efficiently using a simple AI-based prioritization algorithm.

---

## Features

* AI-based subject prioritization
* Smart time allocation based on difficulty, importance, and exam proximity
* Daily study schedule generation
* Simple and clean CLI interface

---

## How It Works

Each subject is evaluated using a priority score, calculated as:

```python
priority = (difficulty * 0.4) + (importance * 0.4) + (1/days_left * 0.2)
```

### Factors:

* Difficulty (1–5): How hard the subject is
* Importance (1–5): Weightage or relevance
* Days Left: Urgency before exam

The planner distributes your total available study time proportionally based on this score.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-study-planner.git
cd ai-study-planner
```

### 2. Run the program

```bash
python main.py
```

No external libraries required (pure Python).

---

## Usage

1. Enter number of subjects
2. Provide details for each subject:

   * Name
   * Difficulty (1–5)
   * Importance (1–5)
   * Days until exam
3. Enter total study hours per day
4. Get your optimized study plan

---

## Example

```
=== AI Study Planner ===

Enter number of subjects: 3

Subject name: Math
Difficulty: 5
Importance: 5
Days until exam: 2

Subject name: English
Difficulty: 2
Importance: 3
Days until exam: 5

Subject name: Physics
Difficulty: 4
Importance: 5
Days until exam: 3

Total study hours per day: 6

Today's Study Plan:
Math: 2.8 hours
Physics: 2.3 hours
English: 0.9 hours
```

---

## Project Structure

```
ai-study-planner/
│
├── main.py        # Main program file
└── README.md      # Project documentation
```

---

## Future Enhancements

* Integration with AI APIs like OpenAI API or Google Gemini
* Performance tracking and analytics
* GUI using Tkinter or PyQt
* Database integration (SQLite/MySQL)
* Mobile or web-based version

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request


---

## Author

Developed by Yash Srivastava

---

## Support

If you found this helpful, consider giving it a star on GitHub.
