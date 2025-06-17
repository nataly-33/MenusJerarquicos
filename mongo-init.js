db = db.getSiblingDB('proyectoavl'); 

db.createUser({
  user: 'nataly-33',
  pwd: 'passWord63',
  roles: [
    {
      role: 'readWrite',
      db: 'proyectoavl',
    },
  ],
});
