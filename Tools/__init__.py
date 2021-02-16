class tools:

    def mean(self, x):
        return float(sum(x)/len(x))

    def mse(self, yr,yp):
        dy = []

        for i in range(0, len(yr)):
            dy.append((yr[i]-yp[i])**2)
        
        return sum(dy)/len(dy)
