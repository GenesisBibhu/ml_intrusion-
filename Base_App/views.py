from django.shortcuts import render, redirect
from Base_App.predict import predict_intrusion  # Import your model prediction function


def check_sum(request):
    if request.method == 'POST':
        try:
            # Get input values from the form and convert to float
            input_data = [
                float(request.POST.get('param1', 0)),
                float(request.POST.get('param2', 0)),
                float(request.POST.get('param3', 0)),
                float(request.POST.get('param4', 0)),
                float(request.POST.get('param5', 0)),
            ]

            # Make prediction using your ML model
            prediction = predict_intrusion(input_data)

            if prediction == 1:
                return render(request, 'alert.html', {
                    'alert_message': 'Suspicious activity detected from IP: 192.168.1.25. Immediate action recommended!',
                    'prediction_result': prediction
                })
            else:
                return render(request, 'safe.html', {
                    'message': 'No suspicious activity detected. System is secure.',
                    'prediction_result': prediction
                })

        except Exception as e:
            # In case of error, return to home with error message
            return render(request, 'home.html', {
                'prediction_text': f"Error: {str(e)}"
            })

    # GET request will just show the form
    return render(request, 'home.html')


def AlertViews(request):
    return render(request, 'alert.html', {
        'alert_message': 'Suspicious activity detected from IP: 192.168.1.25. Immediate action recommended!',
        'prediction_result': 'N/A'
    })


def SafeViews(request):
    return render(request, 'safe.html', {
        'message': 'No suspicious activity detected. System is secure.',
        'prediction_result': 'N/A'
    })


def HomeViews(request):
    return render(request, 'home.html')
