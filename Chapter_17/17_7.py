'''
Given any integer, print an English phrase that describes the integer
(e.g. "One Thousand, Two Hundred Eighty Four").
'''
def intConvert(num):
  
  def hundredsConvert(num):
    ones = { '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
    teens = { '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
    tens = { '1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
    bigs = ['hundred', 'thousand', 'million', 'billion', 'trillion']
  
    answer = ""
    #Convert 100's
    if num >= 100:
      answer += ones[str(num)[0]] + ' hundred'
      num %= 100
    #Convert 10's
    if (num >= 20):
      answer += ' ' + tens[str(num)[0]]
      num %= 10
    #Convert teens
    if (num >= 11) and (num <= 19):
      answer += ' and ' + teens[str(num)]
    #Convert 1's
    if (num >= 1) and (num <=9):
      answer += ' ' + ones[str(num)]
    return answer
    
  ans = ""
  #Convert 1000's
  if num >= 1000 and num <= 999999:
    ans += hundredsConvert(int(str(num)[:-3:])) + " thousand, " + hundredsConvert(int(str(num)[-3::]))
    
  return ans

print(intConvert(234850))
