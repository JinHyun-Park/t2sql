from load_data.schema_loader import load_schema_and_generate_ddls

if __name__ == "__main__":
    load_schema_and_generate_ddls(
        schema_file='mart_user__user_master.json',
        output_file='./metadata/mart_user__user_master_schemas.json',
        dialect='SQLite',
        model_id='anthropic.claude-3-sonnet-20240229-v1:0',
        region_name='us-east-1',
        max_tokens=200000,
        temperature=0.0,
        top_k=250,
        top_p=1
    )