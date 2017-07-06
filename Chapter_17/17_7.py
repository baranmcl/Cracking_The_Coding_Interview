'''
Given any integer, print an English phrase that describes the integer
(e.g. "One Thousand, Two Hundred Eighty Four").
'''
def intConvert(n):
  textNumList = list(str(n))
  ones = { '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
  teens = { '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
  tens = { '10':'ten', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}
  answer = ""
  
  if len(textNumList) > 7:
    return "the number is too big. 7 digits max."
  elif len(textNumList) == 7:
    answer = textNumList[0] + " million"
  
  return textNumList

print(intConvert(45))
