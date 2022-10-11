def magic_calculation(a, b):
    var = 0
        try:
            for i in range(1,3):
            if (i > a):
                raise Exception('Too far')
            else:
                var += (a**b)/i
        except:
            var = (b + a)
            break
    return var
