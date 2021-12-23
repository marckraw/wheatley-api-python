case $1 in

  start)
    python manage.py runserver
    ;;

  install)
    pip install -r requirements.txt
    ;;

  *)
    echo "unknown"
    ;;
esac

