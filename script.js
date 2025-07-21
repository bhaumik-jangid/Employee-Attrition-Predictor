document.addEventListener('DOMContentLoaded', () => {
    const monthlyIncomeInput = document.getElementById('monthlyIncome');
    const ageInput = document.getElementById('age');
    const jobSatisfactionInput = document.getElementById('jobSatisfaction');
    const yearsAtCompanyInput = document.getElementById('yearsAtCompany');
    const overTimeSelect = document.getElementById('overTime');
    const predictButton = document.getElementById('predictButton');
    const resultDiv = document.getElementById('result');
    const messageBox = document.getElementById('messageBox');

    const scalerMean = [11821.532334384858, 44.66482649842271, 2.7365930599369084, 10.25]; 
    const scalerScale = [6595.934337666604, 16.561627365543934, 1.0627111339746103, 7.673531364125289]; 

    const modelCoefficients = [0.07802448002322687, -0.045510965656840756, 0.014831561790689245, 0.07534853498017176, 0.10147590621360404];
    const modelIntercept = -0.04976518020575292;

    function showMessage(message, type = 'error') {
        messageBox.textContent = message;
        messageBox.classList.remove('hidden', 'bg-red-100', 'bg-green-100', 'text-red-700', 'text-green-700');
        if (type === 'error') {
            messageBox.classList.add('bg-red-100', 'border-red-300', 'text-red-700');
        } else {
            messageBox.classList.add('bg-green-100', 'border-green-300', 'text-green-700');
        }
        resultDiv.classList.add('hidden'); 
    }

    function hideMessage() {
        messageBox.classList.add('hidden');
    }

    function sigmoid(z) {
        return 1 / (1 + Math.exp(-z));
    }

    predictButton.addEventListener('click', () => {
        hideMessage(); 

        const monthlyIncome = parseFloat(monthlyIncomeInput.value);
        const age = parseFloat(ageInput.value);
        const jobSatisfaction = parseFloat(jobSatisfactionInput.value);
        const yearsAtCompany = parseFloat(yearsAtCompanyInput.value);
        const overTime = parseInt(overTimeSelect.value); 

        if (isNaN(monthlyIncome) || monthlyIncome < 0 ||
            isNaN(age) || age < 18 || age > 65 ||
            isNaN(jobSatisfaction) || jobSatisfaction < 1 || jobSatisfaction > 4 ||
            isNaN(yearsAtCompany) || yearsAtCompany < 0) {
            showMessage("Please enter valid numerical values for all fields. Age must be between 18-65, Job Satisfaction 1-4.");
            return;
        }

        const featuresToScale = [monthlyIncome, age, jobSatisfaction, yearsAtCompany];
        const scaledFeatures = [];

        for (let i = 0; i < featuresToScale.length; i++) {
            scaledFeatures.push((featuresToScale[i] - scalerMean[i]) / scalerScale[i]);
        }

        const finalFeatures = [
            scaledFeatures[0], 
            scaledFeatures[1],
            scaledFeatures[2], 
            scaledFeatures[3],
            overTime             
        ];

        let z = modelIntercept;
        for (let i = 0; i < finalFeatures.length; i++) {
            z += modelCoefficients[i] * finalFeatures[i];
        }

        const probability = sigmoid(z);

        const prediction = probability >= 0.5 ? 1 : 0;

        resultDiv.classList.remove('hidden');
        if (prediction === 1) {
            resultDiv.textContent = `Prediction: Employee is LIKELY to attrite (Probability: ${probability.toFixed(2)})`;
            resultDiv.classList.remove('bg-blue-50', 'border-blue-200', 'text-blue-800');
            resultDiv.classList.add('bg-red-50', 'border-red-200', 'text-red-800');
        } else {
            resultDiv.textContent = `Prediction: Employee is UNLIKELY to attrite (Probability: ${probability.toFixed(2)})`;
            resultDiv.classList.remove('bg-red-50', 'border-red-200', 'text-red-800');
            resultDiv.classList.add('bg-green-50', 'border-green-200', 'text-green-800');
        }
    });
});
