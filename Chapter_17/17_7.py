'''
Given any integer, print an English phrase that describes the integer
(e.g. "One Thousand, Two Hundred Eighty Four").
'''
def intConvert(n):
  textNumList = list(str(n))
  reversedList = textNumList[::-1]
  ones = { '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
  teens = { '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
  tens = { '1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
  bigs = ['hundred', 'thousand', 'million', 'billion', 'trillion']
  
  if len(textNumList) > 7:
    return "the number is too big. 7 digits max."
  
  answer = ""
  
  return reversedList

print(intConvert(45))
