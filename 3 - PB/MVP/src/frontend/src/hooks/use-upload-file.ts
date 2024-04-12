import { useEffect, useReducer, useRef } from 'react';
import { useToast } from '@/components/ui/use-toast';

interface State<T> {
  data?: T;
  isLoading: boolean;
  progress?: number;
  error?: boolean;
}

type Action<T> =
    | { type: 'loading' }
    | { type: 'fetched'; payload: T }
    | { type: 'error'; payload: boolean }
    | { type: 'progress'; payload: number };

type Options = {
  disabled: boolean | undefined;
};

export const useUploadFile = <T = unknown>(
    url: string,
    resourceUrl: string,
    options: Options
) => {
  const { toast } = useToast();
  const { disabled } = options;

  const cancelRequest = useRef<boolean>(false);

  const initialState: State<T> = {
    error: undefined,
    isLoading: false,
    progress: undefined,
    data: undefined,
  };

  const fetchReducer = (state: State<T>, action: Action<T>): State<T> => {
    switch (action.type) {
      case 'loading':
        return { ...state, isLoading: true };
      case 'fetched':
        return { ...state, data: action.payload, isLoading: false };
      case 'error':
        return { ...state, error: action.payload, isLoading: false };
      case 'progress':
        return { ...state, progress: action.payload };
      default:
        return state;
    }
  };

  const [state, dispatch] = useReducer(fetchReducer, initialState);

  useEffect(() => {
    if (!url || disabled) return;

    cancelRequest.current = false;

    const fetchData = async () => {
      dispatch({ type: 'loading' });

    };

    void fetchData();

    return () => {
      cancelRequest.current = true;
    };
  }, [url]);

  return state;
};
