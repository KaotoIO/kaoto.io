---
title: "Step Extension API"
description: "Documentation for working with the Step Extension API."
draft: false
date: "2022-06-21"
tags:
- Custom View
categories:
- Development
- Extension
- Frontend

---

You can [extend Kaoto with custom views](/docs/add-custom-view) called **Step Extensions**.

Once you have a Step Extension, you will likely want to be able to interact
with Kaoto's state, maybe sharing some of your application's state with
Kaoto as well.

For example, you may want to show a form to configure properties on a step and
then notify Kaoto of the changes so the workflow gets updated.

## Concepts & Usage

For the purposes of this tutorial we will assume you have a very plain
extension [as described here](/docs/add-custom-view). For example,
just a React application that uses Webpack 5.x, and has a basic button component like this:

```jsx
const buttonStyling = {
  backgroundColor: 'BlueViolet',
  color: 'white',
  borderRadius: '25px',
  padding: '20px'
};

const Example = () => {
  return (
    <button style={buttonStyling}>Click to Notify Kaoto</button>
  )
};

export default Example;
```

Keeping in mind that Kaoto is simply an application that is importing your
`Example` component. You can use the **Step Extension API** provided by Kaoto to
interact with the main application, sharing data back and forth.

For example, the **Step Extension API** provides a `notifyKaoto` method, which we
could reference like this from within our component:

```jsx
const Example = (props) => {
  const handleClick = () => {
    if (props.notifyKaoto) {
      props.notifyKaoto('Message from my remote Step Extension!', 'this is the description of the notification', 'success');
    }
  };

  return (
    <button style={buttonStyling} onClick={handleClick}>Click to Notify Kaoto</button>
  )
};
```


If you haven't already done so, you can
[configure Kaoto to use your extension](/docs/add-custom-view).

With Kaoto configured with our extension, you can now use this Step Extension in the step it's configured to be displayed for.
Clicking on the button from the remote application should trigger a notification in Kaoto.

Now that you understand how Step Extensions work, you can check out
[the other methods available on the Step Extension API](https://github.com/KaotoIO/kaoto-ui/blob/main/src/types/index.ts#L85-L107).

If Kaoto doesn't support something you need, you can either
[contribute with the implementation](https://github.com/KaotoIO/kaoto-ui/blob/main/CONTRIBUTING.md#implementing-bug-fixes-or-features)
or [contribute with an issue](https://github.com/KaotoIO/kaoto-ui/blob/main/CONTRIBUTING.md#submit-a-new-issue).
