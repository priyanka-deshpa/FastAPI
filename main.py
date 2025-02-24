from fastapi import FastAPI, HTTPException, Query
from models import Vendor, VendorUpdate
from database import vendors_db
from typing import List
import uvicorn

app =FastAPI()

@app.get("/vendors", response_model=List[Vendor])
def get_vendors():
    return list(vendors_db.values())

@app.get("/vendors/{vendor_id}", response_model=Vendor)
def get_vendor(vendor_id : int):
    if vendor_id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendors_db[vendor_id]

@app.post("/vendors", response_model=Vendor)
def create_vendor(vendor: Vendor):
    if vendor.id in vendors_db:
        raise HTTPException(status_code=400, detail="Vendor already exists")
    vendors_db[vendor.id] = vendor
    return vendor

@app.put("/vendors/{vendor_id}", response_model=Vendor)
def update_vendor(vendor_id: int, vendor_update: VendorUpdate):
    if vendor_id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    
    updated_vendor = vendors_db[vendor_id].copy(update=vendor_update.dict(exclude_unset=True))
    vendors_db[vendor_id] = updated_vendor
    return updated_vendor

@app.delete("/vendors/{vendor_id}")
def delete_vendor(vendor_id: int):
    if vendor_id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    del vendors_db[vendor_id]
    return {"message": "Vendor deleted successfully"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
