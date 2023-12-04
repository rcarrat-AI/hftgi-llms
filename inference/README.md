## Inference 

### Outside the OpenShift/ROSA Cluster

* Grab the Route for HF-TGI Server:

```md
HOST=$(oc get route hf-tgi-server -n llms -o jsonpath='{.spec.host}')
echo $HOST
```

* Ask a question to the LLM (tested with Mistral):

```md
curl https://$HOST/generate \
    -X POST \
    -d '{"inputs":"Give me a recipe of an Italian Carbonara with 10 steps","parameters":{"max_new_tokens":1024}}' \
    -H 'Content-Type: application/json' | jq -r .

{
  "generated_text": ".\n\n## Ingredients\n\n- 1 pound spaghetti\n- 8 ounces pancetta or bacon, diced\n- 1 cup grated Pecorino Romano cheese\n- 4 large eggs\n- 3 cloves garlic, minced\n- 1/2 teaspoon black pepper\n- 1/4 teaspoon salt\n- 2 tablespoons olive oil\n- 1/4 cup chopped fresh parsley\n\n## Instructions\n\n1. Cook the pasta according to package instructions until al dente.\n2. While the pasta is cooking, heat the olive oil in a large skillet over medium heat.\n3. Add the pancetta or bacon and cook until crispy, about 5-7 minutes.\n4. Add the minced garlic and cook for another minute, until fragrant.\n5. In a separate bowl, whisk together the eggs and grated Pecorino Romano cheese.\n6. Drain the pasta and reserve 1 cup of the pasta water.\n7. Add the cooked pasta to the skillet with the pancetta and garlic and toss to combine.\n8. Remove the skillet from the heat and pour in the egg and cheese mixture, tossing quickly to coat the pasta without cooking the eggs.\n9. If the pasta seems dry, add some of the reserved pasta water, 1 tablespoon at a time, until the desired consistency is reached.\n10. Season with black pepper and salt to taste. Serve immediately, garnished with chopped fresh parsley. Enjoy!"
}
```