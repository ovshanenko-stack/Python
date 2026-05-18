def Znach_or_sum(ch1, ch2):
    # Calculate product
    pr = ch1 * ch2

    # Check if product is within the threshold
    if pr <= 1000:
        return pr
    else:
        return ch1 + ch2


# Testing Case 1
resultat= Znach_or_sum(20, 30)
print("Answer is", resultat)

# Testing Case 2
resultat = Znach_or_sum(40, 30)
print("Answer is", resultat)
