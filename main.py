from app.baseEncryption import *
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel, conlist
from typing import Optional

app = FastAPI()

class EncryptData(object):
  def __init__(self):
    pass

  def getEncryptedPayload(self, req, encryptionKey):
    return (encrypt(req, encryptionKey))
  
class Customer(BaseModel):
  first_name: str
  last_name: str
  mobile: str
  country: str
  email: str

class Order(BaseModel):
  amount: float
  reference: str
  description: str
  currency: str

class Payment(BaseModel):
  redirect: str

class Card(BaseModel):
  cvv: str
  card_number: str
  expiry_month: str
  expiry_year: str

class BankTransfer(BaseModel):
  bank_code: str

class PaymentRequest(BaseModel):
  reference: Optional[str]
  payment_option: Optional[str]
  customer: Customer = None
  order: Order = None
  payment: Payment = None
  card: Card = None
  bank_transfer: BankTransfer = None

class ResponseModel(BaseModel):
  data: str

def removeNull(base_model_instance):
  cleaned_data = {key: value for key, value in base_model_instance.dict().items() if value is not None}
  return (cleaned_data)

def checkEncryptionKey(encryption_key: str = Header(None)):
  if encryption_key is None:
    raise HTTPException(status_code=401, detail="Please enter a valid Encryption key.")
  return (encryption_key)

@app.post('/data/encrypt')
async def index(
  payload: PaymentRequest,
  encryption_key: str = Depends(checkEncryptionKey)
):
  cleaned_payload = removeNull(payload)
  
  core = EncryptData()
  encrypted_data = core.getEncryptedPayload(cleaned_payload, encryption_key)
  
  return {"data": encrypted_data}
