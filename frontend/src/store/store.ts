import { configureStore } from '@reduxjs/toolkit';
import { companiesReducer, leadsReducer, campaignsReducer, emailsReducer } from './reducers';

// HUMAN ASSISTANCE NEEDED
// The following code may need additional configuration or optimization for production use.
// Please review and adjust as necessary.

const createStore = () => {
  return configureStore({
    reducer: {
      companies: companiesReducer,
      leads: leadsReducer,
      campaigns: campaignsReducer,
      emails: emailsReducer,
    },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware(),
    devTools: process.env.NODE_ENV !== 'production',
  });
};

export const store = createStore();

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;