def build_prompt(dataset_summary, objective="business insights"):
    return f"""
You are a data analyst. Based on the dataset summary below, generate insightful observations related to {objective}.

Dataset Summary:
- Rows: {dataset_summary['num_rows']}
- Columns: {dataset_summary['columns']}
- Statistics: {dataset_summary['basic_stats']}

Use reasoning and, if needed, suggest visualizations. Present insights clearly.
"""
