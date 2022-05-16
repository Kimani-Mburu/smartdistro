from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse
from django.utils import timezone
from datetime import date, datetime
from django.utils.text import slugify
from django.contrib.auth.models import User


from uuid import uuid4

from UserInformation.models import Customer
from orders.models import Order, Order_other_charge, OtherCharge
from products.models import Product