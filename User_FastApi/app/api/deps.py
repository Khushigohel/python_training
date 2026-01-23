from fastapi import Header, HTTPException

def get_current_user_id(x_user_id: int = Header(...)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="User ID missing")
    return x_user_id
