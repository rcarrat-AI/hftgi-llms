## Inference 

## Using ROSA/OpenShift External Routes

* Grab the Route for HF-TGI Server:

```md
HOST=$(oc get route hf-tgi-server -n llms -o jsonpath='{.spec.host}')
echo $HOST
```

* Check the Model Info:

```md
curl https://$HOST/info | jq -r .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   518  100   518    0     0   1037      0 --:--:-- --:--:-- --:--:--  1050
{
  "model_id": "mistralai/Mistral-7B-Instruct-v0.1",
  "model_sha": "7ad5799710574ba1c1d953eba3077af582f3a773",
  "model_dtype": "torch.float16",
  "model_device_type": "cuda",
  "model_pipeline_tag": "text-generation",
  "max_concurrent_requests": 128,
  "max_best_of": 2,
  "max_stop_sequences": 4,
  "max_input_length": 1024,
  "max_total_tokens": 2048,
  "waiting_served_ratio": 1.2,
  "max_batch_total_tokens": 47920,
  "max_waiting_tokens": 20,
  "validation_workers": 2,
  "version": "1.2.0",
  "sha": "ccd5725a0c0b2ef151d317c86d1f52ad038bbae9",
  "docker_label": "sha-ccd5725"
}
```

* Ask a question to the LLM (tested with Mistral)#:

```md
curl https://$HOST/generate \
    -X POST \
    -d '{"inputs":"Give me a recipe of an Italian Carbonara with 10 steps","parameters":{"max_new_tokens":1024}}' \
    -H 'Content-Type: application/json' | jq -r .

{
  "generated_text": ".\n\n## Ingredients\n\n- 1 pound spaghetti\n- 8 ounces pancetta or bacon, diced\n- 1 cup grated Pecorino Romano cheese\n- 4 large eggs\n- 3 cloves garlic, minced\n- 1/2 teaspoon black pepper\n- 1/4 teaspoon salt\n- 2 tablespoons olive oil\n- 1/4 cup chopped fresh parsley\n\n## Instructions\n\n1. Cook the pasta according to package instructions until al dente.\n2. While the pasta is cooking, heat the olive oil in a large skillet over medium heat.\n3. Add the pancetta or bacon and cook until crispy, about 5-7 minutes.\n4. Add the minced garlic and cook for another minute, until fragrant.\n5. In a separate bowl, whisk together the eggs and grated Pecorino Romano cheese.\n6. Drain the pasta and reserve 1 cup of the pasta water.\n7. Add the cooked pasta to the skillet with the pancetta and garlic and toss to combine.\n8. Remove the skillet from the heat and pour in the egg and cheese mixture, tossing quickly to coat the pasta without cooking the eggs.\n9. If the pasta seems dry, add some of the reserved pasta water, 1 tablespoon at a time, until the desired consistency is reached.\n10. Season with black pepper and salt to taste. Serve immediately, garnished with chopped fresh parsley. Enjoy!"
}
```

## Using Inference Test App

* Check for the Model Info

```md
python app.py info --url https://$HOST 
Model Info:
{
    "model_id": "tiiuae/falcon-7b-instruct",
    "model_sha": "cf4b3c42ce2fdfe24f753f0f0d179202fea59c99",
    "model_dtype": "torch.float16",
    "model_device_type": "cuda",
    "model_pipeline_tag": "text-generation",
    "max_concurrent_requests": 128,
    "max_best_of": 2,
    "max_stop_sequences": 4,
    "max_input_length": 1024,
    "max_total_tokens": 2048,
    "waiting_served_ratio": 1.2,
    "max_batch_total_tokens": 703888,
    "max_waiting_tokens": 20,
    "validation_workers": 2,
    "version": "1.2.0",
    "sha": "ccd5725a0c0b2ef151d317c86d1f52ad038bbae9",
    "docker_label": "sha-ccd5725"
}
```

* Ask a question to be answered:

```md
python app.py generate --url https://$HOST --input "What is OpenShift?" 
Input text: What is OpenShift?

OpenShift is a cloud-native platform for deploying and managing applications. It provides a container-based infrastructure that allows developers to deploy and scale applications quickly and easily. OpenShift also provides a range of tools and services to help developers manage their applications, including source code management, continuous integration, and deployment.
```