document.addEventListener('DOMContentLoaded', function() {
    const surveyForm = document.getElementById('survey_form');
    const purchaseQuestions = document.querySelector('.purchase_questions');

    function togglePurchaseQuestions(show) {
        if (!purchaseQuestions) {
            return;
        }

        purchaseQuestions.style.display = show ? '' : 'none';

        if (!show) {
            const inputs = purchaseQuestions.querySelectorAll('input');
            inputs.forEach(input => {
                if (input.type === 'radio' || input.type === 'checkbox') {
                    input.checked = false;
                }
            });
        }
    }

    const sec1q2Inputs = document.querySelectorAll("input[name='sec1_q2']");
    if (sec1q2Inputs.length > 0) {
        const selected = document.querySelector("input[name='sec1_q2']:checked");
        togglePurchaseQuestions(selected && selected.value === 'yes');

        sec1q2Inputs.forEach(input => {
            input.addEventListener('change', function() {
                togglePurchaseQuestions(this.value === 'yes');
            });
        });
    }

    if (surveyForm) {
        surveyForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(surveyForm);

            const data = {};
            for (let [key, value] of formData.entries()) {
                if (key !== 'csrfmiddlewaretoken') {
                    if (Object.prototype.hasOwnProperty.call(data, key)) {
                        if (!Array.isArray(data[key])) {
                            data[key] = [data[key]];
                        }
                        data[key].push(value);
                    } else {
                        data[key] = value;
                    }
                }
            }

            const csrfToken = formData.get('csrfmiddlewaretoken');

            fetch(surveyForm.action || window.location.pathname, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                return response.json().then(body => {
                    if (!response.ok) {
                        throw new Error(body.error || 'There was an error submitting the survey. Please try again.');
                    }
                    return body;
                });
            })
            .then(result => {
                if (result.success) {
                    window.location.href = '/feedback';
                } else {
                    alert('Error: ' + (result.error || 'There was an error submitting the survey. Please try again.'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert(error.message || 'There was an error submitting the survey. Please try again.');
            });
        });
    }
});
