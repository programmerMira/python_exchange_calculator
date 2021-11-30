class Calculations(object):
    """ Class with math methods """
    
    def addition(self, first, second):
        if first and second:
            return float(first)+float(second)
        else:
            return None
    
    def substraction(self, first, second):
        if first and second:
            return float(first)-float(second)
        else:
            return None

    def multiplication(self, first, second):
        if first and second:
            return float(first)*float(second)
        else:
            return None

    def division(self, first, second):
        if first and second:
            return float(first)/float(second)
        else:
            return None

    def percent(self, first, second):
        if first and second:
            return (float(first)*float(second))/100.0
        else:
            return None

    def power(self, first, second):
        if first and second:
            return float(first)**float(second)
        else:
            return None
    
    def root(self, first, second):
        if first and second:
            return float(first)**(1.0/float(second))
        else:
            return None