import streamlit as st

st.title("Collaborative Quadratic Voting (CQVoting) 🗳️")
st.markdown(
    """
    ### **What is CQVoting? 🗳️**
    Collaborative Quadratic Voting (CQVoting) is a revolutionary voting mechanism designed to allocate resources, prioritize projects, or express preferences in a **fair and impactful way**.  
    Unlike traditional voting systems where each person gets equal votes for every option, CQVoting allows participants to express the **intensity of their preferences**.

    **How does it work?**  
    The more you care about a project, the more votes you can cast for it! But here’s the twist: **the cost of votes increases quadratically**.  
    - **1 vote** = 1 credit  
    - **2 votes** = 4 credits (1 + 3)  
    - **3 votes** = 9 credits (1 + 3 + 5)

    This ensures that while you can support what you love, you’ll need to be strategic with your limited credits.
    ---
    """
)

st.markdown(
    """
    ### **Why CQVoting? 🌍**
    The idea behind CQVoting is to create a voting system that’s not just **fair** but also reflects the **true preferences** of individuals. It was created to:  
    - **Eliminate Bias**: Traditional voting often favors majority opinions. CQVoting gives minorities a voice proportional to their intensity of preference.  
    - **Promote Strategic Thinking**: Limited credits force participants to think carefully about their priorities.  
    - **Encourage Collaboration**: Decisions are no longer about “my way or the highway” but about finding a shared consensus.  
    ---
    """
)

st.markdown(
    """
    ### **When Should You Use CQVoting? 🔍**
    CQVoting is perfect for scenarios where:  
    - You’re allocating a limited budget or resources.  
    - You’re voting on multiple competing projects or proposals.  
    - Decisions need to reflect both **breadth** (what everyone wants) and **depth** (what some people really care about).  

    **Use cases include:**  
    - Crowdsourcing project funding.  
    - Open-source community voting.  
    - Organizational decision-making.  
    ---
    """
)

st.markdown(
    """
    ### **How Does It Work? 🎮**
    1. **Get Your Credits**: Each participant starts with 100 credits.  
    2. **Review Projects**: Check out descriptions, GitHub repos, YouTube demos, and READMEs.  
    3. **Vote**: Allocate your credits wisely! Votes cost more the more you allocate to a single project.  
    4. **Submit**: Once you’ve finalized your votes, hit submit. The projects with the most total support win!  
    ---
    """
)

st.markdown(
    """
    ### **Fun Fact: The Science Behind It! 🧠**
    CQVoting is inspired by the concept of **Quadratic Voting** introduced in the paper “[Quadratic Voting as Efficient Collective Decision-Making](https://arxiv.org/abs/1708.03692)” by E. Glen Weyl. It blends economics, game theory, and ethics to create a voting system that’s not just innovative but also mathematically robust.  

    Want to geek out? Check out the original research: [Read the paper here](https://arxiv.org/abs/1708.03692).  
    ---
    """
)

st.markdown(
    """
    ### **Where Can You Learn More? 🌐**
    - [**GitHub Repository**](https://github.com/UmarYaksambi/CQVoting) – Explore the codebase, raise issues, and contribute!  
    - [**LinkedIn Updates**](www.linkedin.com/in/umaryaksambi) – Follow for the latest news and updates about CQVoting.  
    ---
    """
)

st.markdown(
    """
    ### **Why You’ll Love CQVoting ❤️**
    CQVoting isn’t just about voting; it’s about **redefining how we make decisions together**.  
    Whether you’re part of a tech community, a startup, or an open-source enthusiast, CQVoting brings a fun, strategic, and meaningful approach to collaboration.  

    Join us on this journey to make decision-making more inclusive and impactful! 🚀  
    """
)

st.markdown(
        """
        [☕ Buy Me a Coffee](https://www.buymeacoffee.com/umaryaksambi)
        """, 
        unsafe_allow_html=False
    )

st.markdown("### What would you like to do today?")
st.markdown("### Quick Links")

# Links for actions
st.markdown("[🔗 Vote on Projects](main)", unsafe_allow_html=True)
st.markdown("[📤 Upload a Project](project)", unsafe_allow_html=True)
st.markdown("[📊 View Results](submitted)", unsafe_allow_html=True)

st.markdown("---")