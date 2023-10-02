import base64, json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util.Padding import pad
import xml.etree.ElementTree as ET


def getXmlComponent(xmlstring, _field):
  try:
    # Parse the XML string
    root = ET.fromstring(xmlstring)

    # Find elements with the specified field name
    modulusElements = root.findall(_field)
    modulusValue = ""

    if modulusElements:
      # Extract the Modulus value from the first element
      modulusValue = modulusElements[0].text
    else:
      print("Modulus element not found.")

    return modulusValue

  except Exception as e:
    # Handle exceptions (e.g., parsing errors)
    print("Error:", str(e))
    return ""


def encrypt(data, public_xml):
  try:
    if not data:
      raise Exception("Data sent for encryption is empty")
    # print(data)

    # Decode the Base64 string
    decoded_bytes = base64.b64decode(public_xml)

    # Convert the decoded bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')
    public_xml_key = decoded_string.split('!')[1]

    modulus = getXmlComponent(public_xml_key, "Modulus")
    exponent = getXmlComponent(public_xml_key, "Exponent")

    modulus_bytes = base64.b64decode(modulus)
    exponent_bytes = base64.b64decode(exponent)

    # Create an RSA public key from Modulus and Exponent
    key = RSA.construct((int.from_bytes(modulus_bytes, byteorder='big'),
                         int.from_bytes(exponent_bytes, byteorder='big')))

    # Initialize the Cipher for encryption
    cipher = PKCS1_v1_5.new(key)
    # Encrypt data
    encrypted_bytes = cipher.encrypt(bytes(json.dumps(data), 'utf-8'))
    # print(encrypted_bytes)
    #Convert to base 64 string
    encrypted_bytes_ = base64.b64encode(encrypted_bytes)
    final_encrypted = encrypted_bytes_.decode('utf-8')
    return (final_encrypted)

  except Exception as e:
    raise e
