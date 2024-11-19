import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

llm = ChatOpenAI(
    model="llama3.2:3b",
    base_url="http://192.168.1.6:11434/v1"
)

info_agent = Agent(
    role="Project Manager",
    goal="Transform the non-detailed input given to you about building a smart contract to a very detailed prompt with requirements and whole plan on how to build it which libs to use and every other thing necessary",
    backstory="""
        You are an experienced senior developer who has become the project manager
    """,
    llm=llm
)

task1 = Task(
    description="Write a smart contract for an ERC-20 token which is burnable, pausable, mintable, and has a taxation logic.",
    expected_output="Give me the solidity code with openzeppelin.",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True  # Change 2 to True (or False)
)


result = crew.kickoff()

print("############")
print(result)
