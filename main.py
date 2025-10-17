from uuid import UUID
from typing import List
from fastapi import FastAPI, HTTPException
from models.user import UserRead, UserCreate, UserUpdate  
from models.address import Address, AddressCreate, AddressUpdate

app = FastAPI(title="User Service (skeleton)", version="0.1.0")

NOT_IMPL = HTTPException(status_code=501, detail="Not implemented")

# -----------------------------
# Users
# -----------------------------

# Collection: GET /user
@app.get("/users", response_model=List[UserRead], tags=["users"])
def list_users():
    raise NOT_IMPL

# Collection: POST /users
@app.post("/users", response_model=UserRead, tags=["users"])
def create_user(payload: UserCreate):
    raise NOT_IMPL

# Resource: GET /users/{user_id}
@app.get("/users/{user_id}", response_model=UserRead, tags=["users"])
def get_user(user_id: UUID):
    raise NOT_IMPL

# Resource: PUT /users/{user_id}
@app.put("/users/{user_id}", response_model=UserRead, tags=["users"])
def replace_user(user_id: UUID, payload: UserUpdate):
    raise NOT_IMPL

# Resource: DELETE /users/{user_id}
@app.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: UUID):
    raise NOT_IMPL


# -----------------------------
# Addresses
# -----------------------------

# Collection: GET /addresses
@app.get("/addresses", response_model=List[Address], tags=["addresses"])
def list_addresses():
    raise NOT_IMPL

# Collection: POST /addresses
@app.post("/addresses", response_model=Address, tags=["addresses"])
def create_address(payload: AddressCreate):
    raise NOT_IMPL

# Resource: GET /addresses/{address_id}
@app.get("/addresses/{address_id}", response_model=Address, tags=["addresses"])
def get_address(address_id: UUID):
    raise NOT_IMPL

# Resource: PUT /addresses/{address_id}
@app.put("/addresses/{address_id}", response_model=Address, tags=["addresses"])
def replace_address(address_id: UUID, payload: AddressUpdate):
    raise NOT_IMPL

# Resource: DELETE /addresses/{address_id}
@app.delete("/addresses/{address_id}", tags=["addresses"])
def delete_address(address_id: UUID):
    raise NOT_IMPL
