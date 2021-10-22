from retake.celery import app
from retake.core.models import Process, Part
from retake.core.utils import ProcessData, PROCESS_01, PROCESS_02


@app.task
def get_and_save_process_data():
    process_list = [PROCESS_01, PROCESS_02]
    for process in process_list:
        data = ProcessData(filename=process)
        if Process.objects.filter(number=data.number).exists():
            continue

        p = Process.objects.create(
            number=data.number,
            class_name=data.class_name,
            judge=data.judge,
            subject=data.subject
        )

        for part in data.parts:
            instance, _ = Part.objects.get_or_create(name=part['part'], category=part['category'])
            p.parts.add(instance)

    return True
