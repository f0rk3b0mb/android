ServiceConnection mConnection = new ServiceConnection() {
    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        // Load the class dynamically
        ClassLoader classLoader = getForeignClassLoader(Flag28Activity.this, "io.hextree.attacksurface");
        Class<?> iRemoteServiceClass = classLoader.loadClass("io.hextree.attacksurface.services.IFlag28Interface");

        Class<?> stubClass = null;
        for (Class<?> innerClass : iRemoteServiceClass.getDeclaredClasses()) {
            if (innerClass.getSimpleName().equals("Stub")) {
                stubClass = innerClass;
                break;
            }
        }

        // Get the asInterface method
        Method asInterfaceMethod = stubClass.getDeclaredMethod("asInterface", IBinder.class);

        // Invoke the asInterface method to get the instance of IRemoteService
        Object iRemoteService = asInterfaceMethod.invoke(null, service);

        // Call the init method and get the returned string
        Method openFlagMethod = iRemoteServiceClass.getDeclaredMethod("openFlag");
        boolean initResult = (boolean) openFlagMethod.invoke(iRemoteService);
    }
}