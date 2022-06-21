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

We previously showed you how you can [extend Kaoto with custom views](/docs/add-custom-view) called **Step Extensions**.

Once you have a Step Extension, you will likely want to be able to interact 
with Kaoto's state, maybe sharing some of your application's state with 
Kaoto as well.

## Concepts & Usage

For the purposes of this tutorial we will assume you have a very plain 
extension, just a React application that uses Webpack 5.x, and it has a 
basic button component like this:

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
`Example` component, if the Step Extension API provides a `notifyKaoto` 
method, we could reference it like this from within our component:

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

With Kaoto running and our View Definition catalog pointing to this app (and 
component), we can now view this Step Extension in whichever step it's 
configured to be displayed for. Clicking on the button from the remote 
application should trigger a notification in Kaoto.

Now that you understand how Step Extensions work, you can check out 
the other methods available [here](https://github.com/KaotoIO/kaoto-ui/blob/main/src/api/stepExtensionApi.ts). If we don't 
support something you'd want to see, please let us know by [creating an 
issue](https://github.com/KaotoIO/kaoto-ui/issues/new/choose).


