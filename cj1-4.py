# 4) Session 4 Prompt: Write a Python program that declares a class describing your favorite animal.
# Have the data members of the class represent the following physical parameters of the animal: length
# of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool),
# is it furry? (bool). Write an initialization function that sets the values of the data members when
# an instance of the class is created. Write a member function of the class to print out and describe
# the data members representing the physical characteristics of the animal.

class Ocelot:
    def __init__(self, arm_len, leg_len, eye_num, tail, furry):
        self.arm_len = arm_len  # in centimeters
        self.leg_len = leg_len  # in centimeters
        self.eye_num = eye_num
        self.tail = tail
        self.furry = furry

    def describe(self):
        print("Ocelot Physical Characteristics:")
        print(f"- Arm length: {self.arm_len} cm")
        print(f"- Leg length: {self.leg_len} cm")
        print(f"- Number of eyes: {self.eye_num}")
        print(f"- Has a tail: {'Yes' if self.tail else 'No'}")
        print(f"- Is furry: {'Yes' if self.furry else 'No'}")

my_ocelot = Ocelot(arm_len=40.0, leg_len=45.0, eye_num=2, tail=True, furry=True)

def main():
    my_ocelot.describe()

if __name__ == "__main__":
    main()










