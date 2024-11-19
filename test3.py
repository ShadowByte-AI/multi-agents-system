import requests
import time

# Helper Function to Call Ollama Models for Different Agents
def generate_response(prompt, model="gpt-4"):
    url = f"http://localhost:141434/api/generate" #http://192.168.1.6:141434/api/generate
    payload = {
        "model": model,  # Name of the model (you can replace this with the specific model you want to use)
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()['text'].strip()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

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

# Agent 5: Code Optimization (Improving performance, efficiency, and gas costs)
def agent_5_code_optimizer(code):
    prompt = f"Optimize the following smart contract code for better performance, gas efficiency, and overall improvements: {code}"
    return generate_response(prompt)

# Agent 6: Security Auditor (Checking for vulnerabilities and security issues)
def agent_6_security_auditor(code):
    prompt = f"Audit the following smart contract code for security vulnerabilities and provide recommendations for improvement: {code}"
    return generate_response(prompt)

# Agent 7: Documentation Generator (Creating documentation for the code)
def agent_7_documentation_generator(code):
    prompt = f"Generate documentation for the following smart contract code, including usage instructions and explanations of its functions: {code}"
    return generate_response(prompt)

# Agent 8: Deployment Planner (Providing deployment instructions)
def agent_8_deployment_planner(code):
    prompt = f"Based on the following smart contract code, provide deployment instructions and suggest how to deploy it on Ethereum or Solana: {code}"
    return generate_response(prompt)

# Agent 9: Deployment Executor (Executing deployment process)
def agent_9_deployment_executor(deployment_instructions):
    prompt = f"Execute the following deployment instructions for the smart contract and provide feedback on any issues encountered: {deployment_instructions}"
    return generate_response(prompt)

# Agent 10: Post-Deployment Monitoring (Providing monitoring mechanisms or suggestions)
def agent_10_post_deployment_monitoring(code):
    prompt = f"Provide post-deployment monitoring suggestions for the following smart contract, including potential issues and performance monitoring techniques: {code}"
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
    
    # Step 5: Optimize the code
    print("\nAgent 5: Optimizing the code...")
    optimized_code = agent_5_code_optimizer(code)
    print(f"Optimized Code: {optimized_code}")

    # Step 6: Conduct a security audit
    print("\nAgent 6: Conducting security audit...")
    security_feedback = agent_6_security_auditor(optimized_code)
    print(f"Security Audit Feedback: {security_feedback}")

    # Step 7: Generate documentation for the code
    print("\nAgent 7: Generating documentation...")
    documentation = agent_7_documentation_generator(optimized_code)
    print(f"Documentation: {documentation}")

    # Step 8: Provide deployment instructions
    print("\nAgent 8: Planning deployment...")
    deployment_instructions = agent_8_deployment_planner(optimized_code)
    print(f"Deployment Instructions: {deployment_instructions}")

    # Step 9: Execute deployment
    print("\nAgent 9: Deploying the contract...")
    deployment_feedback = agent_9_deployment_executor(deployment_instructions)
    print(f"Deployment Feedback: {deployment_feedback}")

    # Step 10: Provide post-deployment monitoring suggestions
    print("\nAgent 10: Providing post-deployment monitoring suggestions...")
    post_deployment_feedback = agent_10_post_deployment_monitoring(optimized_code)
    print(f"Post-Deployment Monitoring Feedback: {post_deployment_feedback}")

    # Final refined code after all steps
    print("\nFinal Code after Testing, Refining, Optimization, and Deployment:")
    print(optimized_code)
    return optimized_code

# Example Usage
if __name__ == "__main__":
    initial_prompt = "Create a smart contract for a decentralized auction system"
    final_code = main_workflow(initial_prompt)
    print(f"\nFinal Resulting Code:\n{final_code}")
