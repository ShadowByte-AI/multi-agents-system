import openai
import time

# Setup OpenAI API
openai.api_key = "your-openai-api-key"

# Helper Function to Call GPT Models for Different Agents
def generate_response(prompt, model="gpt-4"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Agent 1: Prompt Improver (Expanding the Initial Idea into a Full Plan)
def agent_1_prompt_improver(one_line_prompt):
    prompt = f"Expand the following idea into a full development plan for a smart contract or decentralized app (DApp): {one_line_prompt}"
    return generate_response(prompt)

# Agent 2: Code Developer (Generating Solidity or Rust Code Based on the Plan)
def agent_2_code_developer(plan):
    prompt = f"Based on the following development plan, generate the required Solidity or Rust code for a smart contract or DApp: {plan}"
    return generate_response(prompt)

# Agent 3: Tester (Providing Testing and Feedback on the Code)
def agent_3_tester(code):
    prompt = f"Test the following smart contract or DApp code and provide feedback on any errors or improvements needed: {code}"
    return generate_response(prompt)

# Agent 4: Developer (Refining the Code Based on Tester Feedback)
def agent_4_developer(feedback):
    prompt = f"Refactor the code based on the following tester feedback and improve it: {feedback}"
    return generate_response(prompt)

# Main Workflow
def main_workflow(one_line_prompt):
    # Step 1: Improve the initial prompt into a full plan
    print("Agent 1: Improving prompt into a full plan...")
    development_plan = agent_1_prompt_improver(one_line_prompt)
    print(f"Development Plan: {development_plan}")

    # Step 2: Generate the required code based on the plan
    print("\nAgent 2: Generating code...")
    code = agent_2_code_developer(development_plan)
    print(f"Generated Code: {code}")

    # Step 3: Test the code
    print("\nAgent 3: Testing the code...")
    tester_feedback = agent_3_tester(code)
    print(f"Tester Feedback: {tester_feedback}")

    # Step 4: Developer loop (refining code based on feedback)
    iteration_count = 0
    while "error" in tester_feedback.lower() or "improvement" in tester_feedback.lower():
        print(f"\nDeveloper loop iteration {iteration_count + 1}...")
        code = agent_4_developer(tester_feedback)
        print(f"Refined Code: {code}")
        
        # Re-test the code
        tester_feedback = agent_3_tester(code)
        print(f"New Tester Feedback: {tester_feedback}")
        
        iteration_count += 1
        time.sleep(1)  # Simulate delay for testing/refining process
    
    # Final refined code after successful testing
    print("\nFinal Code after Testing and Refining:")
    print(code)
    return code

# Example Usage
if __name__ == "__main__":
    initial_prompt = "Create a smart contract for a decentralized auction system"
    final_code = main_workflow(initial_prompt)
    print(f"\nFinal Resulting Code:\n{final_code}")
