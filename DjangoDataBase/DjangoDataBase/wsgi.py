"""
WSGI config for DjangoDataBase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import threading
from django.core.wsgi import get_wsgi_application
from DjangoDataBase.tasks import schedulTask
from DjangoDataBase.tasks import insert_data_from_csv
from DjangoDataBase.tasks import make_predictions
from DjangoDataBase.tasks import data_after_prediction
from DjangoDataBase.tasks import data_after_prediction1
from .tasks import RepeatTimer

insert_data_from_csv()
scaled_predictions, predictions_list = make_predictions()
data_after_prediction(scaled_predictions)
data_after_prediction1(predictions_list)
t = RepeatTimer(300.0, schedulTask)
t.start()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoDataBase.settings')

application = get_wsgi_application()
