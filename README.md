This is a repository for roadwarden translate server.

## To run:

1. Clone the repository:

```
git clone https://github.com/player21o/roadwarden-translate-server.git
```

2. `cd` into the repository and install modules:

```
npm i
```

3. Create `config.ts` in `app` folder with following contents:

```
export const config = {
  discord: {
    auth_link:
      "authlink",
    redirect_url: "redirect",
    token:
      "token",
    client: {
      id: "id",
      secret: "secret",
    },
  },
};

```

4. Create `.env` in the root folder and specify postgresql connection link:

```
DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<tablename>
```

5. Push database schema:

```
npx drizzle-kit push
```

6. Run server:

```
tsx app
```

Parsing and maintaining the files is done via [rd-kit](https://github.com/player21o/roadwarden-translate-server/tree/main/rd-kit)
