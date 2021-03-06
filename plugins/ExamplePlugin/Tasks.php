<?php
/**
 * Piwik - Open source web analytics
 *
 * @link http://piwik.org
 * @license http://www.gnu.org/licenses/gpl-3.0.html GPL v3 or later
 *
 */
namespace Piwik\Plugins\ExamplePlugin;

class Tasks extends \Piwik\Plugin\Tasks
{
    public function schedule()
    {
        $this->hourly('myTask');  // method will be executed once every hour
        $this->daily('myTask');   // method will be executed every daily
        $this->weekly('myTask');  // method will be executed once every weekly
        $this->monthly('myTask'); // method will be executed once every monthly

        // pass a parameter to the task
        $this->weekly('myTaskWithParam', 'anystring');

        // specify a different priority
        $this->monthly('myTask', null, self::LOWEST_PRIORITY);
        $this->monthly('myTaskWithParam', 'anystring', self::HIGH_PRIORITY);
    }

    public function myTask()
    {
        // do something
    }

    public function myTaskWithParam($param)
    {
        // do something
    }
}