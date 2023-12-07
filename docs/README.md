# Finding the area and perimeter of geometric shapes

## Description
Functions used to calculate the area and perimeter of geometric shapes(rectangle and triangle)

## Math Formulas

### Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Functions

### circle.py

- area(r)

Description: calculates area of a circle with giving radius=r.

Example:

>>>from geometric_lib import circle

r = 1.0
print(area(r))

'3.141592653589793'

- perimeter(r)

Description: calculates perimeter of a circle with giving radius=r.

Example:

>>>from geometric_lib import circle

r = 1.0
print(perimeter(r))

'6.283185307179586'

### rectangle.py

- area(a, b)

Description: calculates area of a circle with given length=a and width=b.

Example:

>>>from geometric_lib import circle

a = 1.0
b = 2.0

print(area(a, b))

'2.0'

- perimeter(a, b)

Description: calculates perimeter of a circle with given length=a and width=b.

Example:

>>>from geometric_lib import circle

a = 1.0
b = 2.0

print(perimeter(a, b))

'6.0'

### square.py

- area(a)

Description: calculates area of a circle with given side=a.

Example:

>>>from geometric_lib import circle

a = 1.0

print(area(a))

'1.0'

- perimeter(a)

Description: calculates perimeter of a circle with given side=a.

Example:

>>>from geometric_lib import circle

a = 1.0

print(perimeter(a))

'4.0'

### triangle.py

- area(a, h)

Description: calculates area of a triangle with given side=a and height=h.

Example:

>>>from geometric_lib import circle

a = 1.0
h = 2.0

print(area(a, h))

'1.0'

- perimeter(a)

Description: calculates perimeter of a triangle with given sides=a, b, c.

Example:

>>>from geometric_lib import circle

a = 1.0
b = 2.0
c = 3.0

print(perimeter(a, b, c))

'6.0'

## Commits History 

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
    
- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
    
- commit 2d81844c2319991446be6f1c301cbf5f4c2f3e78
Author: bcsergey <buchnewserg@yandex.ru>
Date:   Thu Dec 7 05:20:31 2023 +0300

    feat: add rectangle geometry
    

- commit d10f7713186d885fcbb6423c07820b0c59fe4ad1 (origin/main, origin/documentation_264984, origin/HEAD, main)
Author: bcsergey <buchnewserg@yandex.ru>
Date:   Thu Dec 7 05:25:47 2023 +0300

    fix: fix rectangle perimeter calculation / add triangle geometry
    
- commit 67060640257e32fca02ecdc1797055d37043d5e3 (HEAD -> documentation_264984)
Author: bcsergey <buchnewserg@yandex.ru>
Date:   Thu Dec 7 09:07:53 2023 +0300

    docs: add documentation to geometry functions

