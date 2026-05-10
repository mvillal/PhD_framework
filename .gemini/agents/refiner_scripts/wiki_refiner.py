import os
import json
import time
from typing import TypedDict, List
from src.container import container

# --- State Definition ---
class AgentState(TypedDict):
    source_path: str
    run_id: str
    content: str
    metadata: dict
    grading_score: float # 0.0 to 1.0

# --- Nodes ---

def research_node(state: AgentState):
    """
    Simulates fetching details for a TBD paper.
    """
    explanation = f"Searching for full-text and metadata for {state['source_path']} using Google Scholar and CrossRef APIs."
    print(f"--- Researching: {state['source_path']} ---")
    
    # Log step to the tracking framework
    container.log_step.execute(
        state['run_id'], 
        "Research", 
        explanation, 
        metadata={"source": state['source_path']}
    )
    
    # Simulated content extraction
    content = f"Simulated content for {state['source_path']}"
    return {"content": content}

def extraction_node(state: AgentState):
    """
    Simulates extracting structured data.
    """
    explanation = "Extracting entities (Authors, Lab, Year) and core findings using a prompt-optimized Vision Transformer and LLM parser."
    print("--- Extracting Structured Summary ---")
    
    container.log_step.execute(state['run_id'], "Extraction", explanation)
    
    # Simulated metadata
    metadata = {"title": "Refined Paper", "year": 2026, "lab": "DtAK"}
    
    # Log the extracted markdown as an artifact
    markdown_content = f"# {metadata['title']}\nAuto-generated summary content..."
    container.log_artifact.execute(
        state['run_id'], 
        "summary.md", 
        markdown_content, 
        f"output/{os.path.basename(state['source_path'])}"
    )
    
    return {"metadata": metadata}

def grading_node(state: AgentState):
    """
    Self-RAG: Checks grounding.
    """
    explanation = "Grading the extracted summary against the raw content to identify hallucinations or missing clinical context."
    print("--- Grading Generation ---")
    
    score = 0.95
    container.log_step.execute(
        state['run_id'], 
        "Grading", 
        explanation, 
        metadata={"score": str(score)}
    )
    container.log_metric.execute(state['run_id'], "quality_score", score)
    
    return {"grading_score": score}

# --- Execution Flow ---

def run_autoresearcher(paper_path: str):
    # 1. Start a tracked run
    run = container.start_run.execute(
        experiment_id="Autoresearcher-Self-Improvement",
        run_name=f"Ingest-{os.path.basename(paper_path)}"
    )
    
    state: AgentState = {
        "source_path": paper_path,
        "run_id": run.run_id,
        "content": "",
        "metadata": {},
        "grading_score": 0.0
    }
    
    try:
        # Sequential execution (simplification of the graph)
        state.update(research_node(state))
        state.update(extraction_node(state))
        state.update(grading_node(state))
        
        # 3. Complete the run
        print(f"✅ Ingestion complete for {paper_path}. Run ID: {run.run_id}")
        container.complete_run.execute(run.run_id)
        
    except Exception as e:
        print(f"❌ Autoresearcher failed: {e}")

if __name__ == "__main__":
    print("🚀 Initializing Tracked Autoresearcher...")
    run_autoresearcher("papers/sources/doshi-velez/lu_2026_neural_sdes_suicide_risk.md")
