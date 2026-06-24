workout_tracker = {
    "Pushups": {"completed": 40, "target": 50},
    "Running": {"completed": 5, "target": 5},
    "Water Intake": {"completed": 2, "target": 4}
}

def display_progress(tracker):
    print("Display Current Progress")
    for event, stats in tracker.items():
        print(f'Habit : {event} --- Statistics : Completed - {stats['completed']}, Target - {stats['target']}')

display_progress(workout_tracker)