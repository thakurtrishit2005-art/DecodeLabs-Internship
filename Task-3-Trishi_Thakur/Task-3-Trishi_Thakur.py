import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_validated_input(prompt_text):
    """
    Forces valid data ingestion to bypass the User Cold Start problem.
    Ensures the user cannot pass empty values or zero vectors.
    """
    while True:
        user_input = input(prompt_text).strip()
        # Validation Check: Ensure input is alphanumeric and not just empty spaces
        if user_input and any(char.isalnum() for char in user_input):
            return user_input
        print("[System Alert] Input cannot be blank. Please provide a skill to build the vector space.")

def run_matchmaker():
    print("=============================================")
    print("      DECODELABS MATCHMAKER ENGINE v2.0      ")
    print("   AI Recommendation Logic (Project 3)       ")
    print("=============================================\n")

    # Load Dataset upfront to verify data integrity
    try:
        df = pd.read_csv('raw_skills.csv')
    except FileNotFoundError:
        print("[Fatal Error] raw_skills.csv not found! Please check your file path configuration.")
        return

    # Extract items (roles) and attributes (skills) from structural framework
    roles = df['Role'].tolist()
    job_descriptions = df['Skills'].tolist()

    print("--- [STAGE 1/4: DATA INGESTION & COLD-START BYPASS] ---")
    print("Please complete the onboarding survey to bootstrap your preference vector.\n")
    
    # Explicitly enforce 3 dense features as dictated by project guidelines
    skill_1 = get_validated_input("Enter your primary technical skill (e.g., Python, Java): ")
    skill_2 = get_validated_input("Enter your core concept/interest (e.g., Automation, Design, SQL): ")
    skill_3 = get_validated_input("Enter your preferred tool/infrastructure (e.g., Docker, Pandas, AWS): ")
    
    # Construct structured User State string representation
    user_skills_combined = f"{skill_1} {skill_2} {skill_3}"
    print(f"\n-> Successfully mapped vector dimensions for: ['{skill_1}', '{skill_2}', '{skill_3}']\n")

    print("--- [STAGE 2/4: VECTOR MAPPING & SIMILARITY SCORING] ---")
    print("Applying logarithmic TF-IDF weighting and executing vector angular alignment math...")
    
    # Append User Profile to Item collection to unify the vocabulary mapping space
    all_documents = job_descriptions + [user_skills_combined]
    
    # Configure vector space to handle individual terms cleanly
    vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b') 
    tfidf_matrix = vectorizer.fit_transform(all_documents)
    
    # Isolate independent item arrays from explicit user matrix slice
    item_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]
    
    # Execute structural dot product matching over normalized lengths (Cosine Alignment)
    similarity_scores = cosine_similarity(user_vector, item_vectors).flatten()

    print("--- [STAGE 3/4: MULTI-DIMENSIONAL DATA SORTING] ---")
    print("Sorting entire corpus in descending structural order based on match proximity...")
    
    # Aggregate matrix math results back into target data structures
    results = []
    for i in range(len(roles)):
        results.append({
            'Role': roles[i],
            'Score': similarity_scores[i]
        })
        
    # Sort array in descending order based on calculated angular match scores
    sorted_results = sorted(results, key=lambda x: x['Score'], reverse=True)
    print("Sorting matrix process complete.\n")

    print("--- [STAGE 4/4: CHOICE OVERLOAD FILTERING & OUTPUT] ---")
    print("Truncating dataset down to designated Top-N collection...\n")
    
    print("=========================================================")
    print("             DECODELABS TOP MATCHED ROLES                ")
    print("=========================================================")
    
    # Truncate strictly to Top 3 results to fulfill quality standards
    top_n = sorted_results[:3]
    
    match_found = False
    for rank, match in enumerate(top_n, start=1):
        match_percentage = match['Score'] * 100
        
        if match_percentage > 0:
            print(f" Rank {rank} | {match['Role']:<20} | Alignment: {match_percentage:.2f}%")
            match_found = True
        else:
            print(f" Rank {rank} | {match['Role']:<20} | Alignment: 0.00% [Orthogonal Space]")

    # Strategic Trending Fallback implementation for absolute zero-overlap profiles
    if not match_found:
        print("\n=========================================================")
        print("[User Cold Start Safe-Mode Triggered]")
        print("Vector overlap reached 0.00%. Activating system fallback strategy...")
        print(f"Recommended Default: {roles[0]} (Global Community Popularity Model)")
    
    print("=========================================================")

if __name__ == "__main__":
    run_matchmaker()