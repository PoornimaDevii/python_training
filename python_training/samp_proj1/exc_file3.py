
import sys

try:
    f = open("myfile.txt")
    val = int(f.read().strip())
    f.close()
except FileNotFoundError:
    print("No such file")
except ValueError:
    print("Not a number")
except:
    print(sys.exc_info()[0])
    raise

# or

try:
    f = open("myfile.txt")
    val = int(f.read().strip())

except FileNotFoundError:
    print("No such file")
except ValueError:
    print("Not a number")
except:
    print(sys.exc_info()[0])
    raise

else:
    res = 6/val
    print("Res is", res)
    f.close()
