class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ans = self.inc_second(time)
        while True:
        	if self.isvalid(ans, time):
        		return ans
        	ans = self.inc_second(ans)
        return None

    def inc_second(self, time):
    	hour = int(time.split(":")[0])
    	minute = int(time.split(":")[1])
    	minute += 1
    	if minute == 60:
    		minute = 0
    		hour += 1
    		if hour == 24:
    			hour = 0
    	if hour < 10:
    		hour = "0{}".format(hour)
    	else:
    		hour = str(hour)
    	if minute < 10:
    		minute = "0{}".format(minute)
    	else:
    		minute = str(minute)
    	return "{}:{}".format(hour, minute)

    def isvalid(self, ans, time):
    	digits = [char for char in time]
    	for char in ans:
    		if char not in digits:
    			return False
    	return True

sol = Solution()
print(sol.nextClosestTime("23:59"))