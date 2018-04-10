class Solution(object):
	def intToRoman(self, num):
		result = ""
		while num > 0:
			while num >= 1000:
				result = result + "M"
				num = num - 1000
			if num >= 900:
				result = result + "CM"
				num = num - 900
			if num >= 500:
				result = result + "D"
				num = num - 500
			if num >= 400:
				result = result + "CD"
				num = num - 400
			while num >= 100:
				result = result + "C"
				num = num - 100
			if num >= 90:
				result = result + "XC"
				num = num - 90
			if num >= 50:
				result = result + "L"
				num = num - 50
			if num >= 40:
				result = result + "XL"
				num = num - 40
			while num >= 10:
				result = result + "X"
				num = num - 10
			if num >= 9:
				result = result + "IX"
				num = num - 9
			if num >= 5:
				result = result + "V"
				num = num - 5
			if num >= 4:
				result = result + "IV"
				num = num - 4
			while num >= 1:
				result = result + "I"
				num = num - 1
		return result



