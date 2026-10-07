#!/usr/bin/env python3
"""
Indian Constitution + BNS RAG Query Tool
Ask questions about Indian constitutional law and BNS (replaced IPC)
"""

import os
import sys
import argparse
import re

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)

def query_legal_corpus(query, k=5):
    """Query both Constitution and BNS"""
    try:
        print("🔄 Loading Indian Legal Corpus (Constitution + BNS)...")
        
        from langchain_community.embeddings import HuggingFaceEmbeddings
        from langchain_community.vectorstores import Chroma
        
        # Use combined database
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Check which DB exists
        combined_db_path = os.path.join(SKILL_DIR, "embeddings", "combined_db")
        old_db_path = os.path.join(SKILL_DIR, "embeddings", "chroma_db")
        
        if os.path.exists(combined_db_path):
            db_path = combined_db_path
            docs = "Constitution + BNS 2023"
        else:
            db_path = old_db_path
            docs = "Constitution only"
        
        vectorstore = Chroma(
            persist_directory=db_path,
            embedding_function=embeddings
        )
        
        print(f"✅ Loaded: {docs}")
        
        print(f"\n🔍 Query: {query}")
        print("=" * 60)
        
        # Search
        docs_results = vectorstore.similarity_search(query, k=k)
        
        print(f"📚 Found {len(docs_results)} relevant legal provisions:\n")
        
        all_content = []
        sources = []
        
        for i, doc in enumerate(docs_results, 1):
            content = doc.page_content
            all_content.append(content)
            
            # Determine source
            if "BNS PAGE" in content or "BHARATIYA NYAYA SANHITA" in content:
                source = "BNS 2023"
                color = "🔴"
            elif "=== THE CONSTITUTION" in content:
                source = "Constitution"
                color = "🟢"
            else:
                source = "Constitution/BNS"
                color = "📖"
            
            sources.append(source)
            
            # Extract article/section numbers
            articles = re.findall(r'Article\s+\d+[A-Z]?', content)
            sections = re.findall(r'Section\s+\d+[A-Z]?', content)
            
            print(f"--- Result {i} [{color} {source}] ---")
            if articles:
                print(f"📜 Articles: {', '.join(set(articles)[:3])}")
            if sections:
                print(f"§ Sections: {', '.join(set(sections)[:3])}")
            print(content[:600] + "..." if len(content) > 600 else content)
            print()
        
        # Generate summary
        print("=" * 60)
        print("⚖️  LEGAL ANALYSIS")
        print("=" * 60)
        
        # Identify unique sources
        unique_sources = set(sources)
        print(f"📖 Sources: {', '.join(unique_sources)}")
        
        # Extract all articles and sections
        all_articles = re.findall(r'Article\s+\d+[A-Z]?', '\n'.join(all_content))
        all_sections = re.findall(r'Section\s+\d+[A-Z]?', '\n'.join(all_content))
        
        if all_articles:
            print(f"📜 Constitutional Articles: {', '.join(sorted(set(all_articles))[:5])}")
        if all_sections:
            print(f"§ BNS Sections: {', '.join(sorted(set(all_sections))[:5])}")
        
        # Generate synthesized answer
        print(f"\n📝 Answer to: \"{query}\"")
        print("-" * 60)
        
        # Use first result as primary answer
        if docs_results:
            primary = docs_results[0].page_content[:800]
            print(primary + "..." if len(docs_results[0].page_content) > 800 else primary)
        
        print("\n⚠️  Disclaimer: This is for informational purposes only.")
        print("   Consult a qualified legal professional for legal advice.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    parser = argparse.ArgumentParser(
        description="Query Indian Constitution and BNS (Bharatiya Nyaya Sanhita)"
    )
    parser.add_argument("query", help="Your legal question")
    parser.add_argument("-k", type=int, default=5, 
                       help="Number of results (default: 5)")
    
    args = parser.parse_args()
    query_legal_corpus(args.query, args.k)

if __name__ == "__main__":
    main()
