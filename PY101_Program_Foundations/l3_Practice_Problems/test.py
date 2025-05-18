munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_member_demographics(demo_dict, family_member):
    if family_member in demo_dict:
        demo_dict[family_member]["age"] += 42
        demo_dict[family_member]["gender"] = "other"

    print(f'{family_member} is {demo_dict[family_member]}')

mess_with_member_demographics(munsters, "Herman")