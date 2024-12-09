# Collaborative Quadratic Voting (CQVoting) 🗳️

Welcome to the **Collaborative Quadratic Voting (CQVoting)** project! If you’ve ever wanted to make decisions with your friends, team, or community in a way that’s fair and fun, then you’re in the right place! CQVoting combines **Quadratic Voting** with a **collaborative twist** to make decision-making smarter and more democratic. It’s all about fairness, fun, and amplifying everyone’s voice!

## What is Collaborative Quadratic Voting? 🤔

At its core, **CQVoting** is like a superpower for voting. You get a fixed amount of credits (say, **100 credits**) to vote on different issues, and you distribute those credits in a **quadratic manner**. 

### **Quadratic Voting (QV)**:

In normal voting, you get 1 vote for each issue, simple, right? But in **Quadratic Voting**, users express their preference intensity with a fixed amount of credits (100 credits), which they can allocate across different options. The catch is that votes increase in cost based on the number of votes you cast! This quadratic cost ensures that no one person can dominate the process just by casting many votes.

For example, if you decide to spend your credits on voting for different issues:

- 1 vote costs 1 credit
- 2 votes for the same issue costs 4 credits (not just 2)
- 3 votes cost 9 credits, and so on!

The more votes you assign, the more it costs, which means you can’t just “buy” votes. This makes sure that people are thoughtful and intentional with how they distribute their votes.


Because CQVoting makes decision-making more **democratic**, **fun**, and **fair**! Whether you're making group decisions with your friends, voting on ideas at work, or just having a friendly poll, CQVoting helps you make smarter choices. Plus, it’s pretty awesome to see how votes stack up when everyone chips in! 💪

## 🎯 Features

- **Smart Voting**: Allocate votes based on how strongly you feel, but with a quadratic twist! The more votes you cast, the higher the cost gets, keeping everything balanced.
- **Open-Source Awesomeness**: This project is open to contributions! Help us make it even better by submitting pull requests, reporting bugs, or adding features!

## 🚀 How to Get Started

Ready to jump into the fun? Here’s how to get CQVoting up and running:

1. **Clone the Repository**: 
   Grab the repo and dive in!

   ```bash
   git clone https://github.com/UmarYaksambi/CQVoting.git
   cd CQVoting
   ```

2. **Install the Dependencies**: 
   Let’s get everything installed so you can run the system smoothly.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Backend**: 
   Fire up the backend server using **Uvicorn**. This handles all the heavy lifting!

   ```bash
    uvicorn backend.main:app --reload --port 8080
   ```

   Your backend will now be running at `http://localhost:8080`.

4. **Run the Frontend (Streamlit)**: 
   Now, let’s get the fun part going with **Streamlit**. Open up the voting interface and start casting your votes!

   ```bash
    streamlit run frontend/app.py
   ```

   This will launch the app in your browser where all the action happens! 🔥



---

### **How Does Collaborative Quadratic Voting Work?**

Imagine you have three options to vote on: **A**, **B**, and **C**.

Each user has a fixed amount of **credits** (let's say 100) to allocate across these options. The key difference is that voting **quadratically** means that the cost of votes increases as you vote more for a particular option.

---

Here's the simplified example with user votes in points:

---

### Example:

Let's say **User 1** and **User 2** both have 100 credits to distribute across options A, B, and C.

- **User 1** LOVES **A** and gives 9 credits for **A** (3 votes), and 4 credits for **B** (2 votes).  
  **User 1's votes**:  
  - A: 9 credits  
  - B: 4 credits  
  - Total spent: 13 credits

- **User 2** likes **A** too, but not as much. They give 4 credits for **A** (2 votes), 1 credits for **B** (1 vote), and 4 credits for **C** (2 votes).  
  **User 2's votes**:  
  - A: 4 credits  
  - B: 1 credits  
  - C: 4 credits  
  - Total spent: 9 credits

After the credits are spent, we **normalize** the votes, which means we adjust the total number of votes to ensure that they are comparable across users. Normalization makes sure that the influence of each user’s votes is fair and proportional.

### **How Does Normalization Work?**
Once all the users cast their votes, the system calculates the total number of votes for each option and normalizes them. Normalizing means adjusting the votes based on the total credits used by all users, making sure that no one’s votes dominate the system because they had more credits or cast more votes.

### **Why Is This Fair?**
This approach ensures that everyone’s votes are **proportional** to their preferences and the quadratic nature of the voting system keeps it fair, as the cost of casting additional votes increases. No one can just cast a large number of votes to overwhelm others, which ensures that the decision-making process stays **democratic and balanced**.

---

## 🎉 Contributing

Got ideas to make this even more awesome? Contribute to the project! Whether it’s bug fixes, cool new features, or just adding to the fun, we welcome all contributions! 🎨✨

- **Report Issues**: Found a bug? Let us know!
- **Suggest Features**: Have an idea to make CQV better? We’re all ears! 👂
- **Pull Requests**: Feel like improving the code? Open a PR, and let’s make this project rock even harder! 🎸

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
