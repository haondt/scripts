# hx-rename

HTMX extension to rename form parameters before sending. The extension intercepts `htmx:configRequest` to transform parameter names before the request is sent.

## Usage

```html
<script src="hx-rename.js"></script>

<form hx-post="/submit" hx-rename="oldName:newName,user_email:email">
    <input name="oldName" value="test">
    <input name="user_email" value="john@example.com">
</form>
```

The above form sends: `newName=test&email=john%40example.com`.

Parameters with the same target name are joined into arrays:

```html
<form hx-post="/submit" hx-rename="first:name,last:name">
    <input name="first" value="John">
    <input name="last" value="Doe">
    <input name="name" value="existing">
</form>
```

Sends: `name=existing&name=John&name=Doe`.

